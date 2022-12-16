import os
import unittest
import tempfile

from tia_portal.client import Client
import tia_portal.exceptions as tia_e
from tia_portal.test import TEST_VERSION


class TestClient(unittest.TestCase):
    def test_load_client(self) -> Client:
        try:
            client = Client(TEST_VERSION)
        except tia_e.TIALibraryNotFound:
            self.fail("Could not load TIA library")

        return client

    def test_init(self):
        client = self.test_load_client()
        self.assertIsInstance(client.session, client.tia.TiaPortal)
        client.close()

    def test_open_gui(self):
        client = self.test_load_client()
        client.open_gui()
        if client.session is None:
            self.fail("Session is None")
        self.assertEqual(client.session.GetCurrentProcess().Mode, client.tia.TiaPortalMode.WithUserInterface)
        client.close()

    def test_close_gui(self):
        client = self.test_load_client()
        self.test_open_gui()
        client.open_gui()
        client.close_gui()
        if client.session is None:
            self.fail("Session is None")
        self.assertEqual(client.session.GetCurrentProcess().Mode, client.tia.TiaPortalMode.WithoutUserInterface)
        client.close()

    def test_create_project(self):
        client = self.test_load_client()
        temp_dir = tempfile.TemporaryDirectory()
        client.create_project(temp_dir.name, "test")
        self.assertTrue(os.path.exists(os.path.join(temp_dir.name, "test")))
        self.assertIsInstance(client.project, client.tia.Project)
        client.close()
        temp_dir.cleanup()

    def test_open_project(self):
        client = self.test_load_client()
        temp_dir = tempfile.TemporaryDirectory()
        self.assertRaises(tia_e.TIAProjectNotFound, client.open_project, temp_dir.name, "test")
        self.test_create_project()
        client.create_project(temp_dir.name, "test")
        client.open_project(temp_dir.name, "test")
        self.assertIsInstance(client.project, client.tia.Project)
        client.close()
        temp_dir.cleanup()

    def test_close_project(self):
        client = self.test_load_client()
        temp_dir = tempfile.TemporaryDirectory()
        self.test_create_project()
        client.create_project(temp_dir.name, "test")
        self.test_open_project()
        client.open_project(temp_dir.name, "test")
        client.close_project()
        self.assertIsNone(client.project)
        client.close()
        temp_dir.cleanup()

    def test_close(self):
        client = self.test_load_client()
        client.close()
        self.assertIsNone(client.session)


if __name__ == "__main__":
    unittest.main()

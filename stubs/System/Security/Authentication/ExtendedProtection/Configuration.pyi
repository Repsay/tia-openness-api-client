# encoding: utf-8
# module System.Security.Authentication.ExtendedProtection.Configuration calls itself Configuration
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExtendedProtectionPolicyElement(ConfigurationElement):
    """
    The System.Security.Authentication.ExtendedProtection.Configuration.ExtendedProtectionPolicyElement class represents a configuration element for an System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy.

    ExtendedProtectionPolicyElement()
    """
    def BuildPolicy(self):
        """
        BuildPolicy(self: ExtendedProtectionPolicyElement) -> ExtendedProtectionPolicy

            The System.Security.Authentication.ExtendedProtection.Configuration.ExtendedProtectionPolicyElement.BuildPolicy method builds a new 

             System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy instance based on the properties set on the 

             System.Security.Authentication.ExtendedProtection.Configuration.ExtendedProtectionPolicyElement class.

            Returns: A new System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy instance that represents the extended protection policy created.
        """
        ...

    @property
    def CustomServiceNames(self):
        """
        Gets or sets the custom Service Provider Name (SPN) list used to match against a client's SPN for this configuration policy element.

        Get: CustomServiceNames(self: ExtendedProtectionPolicyElement) -> ServiceNameElementCollection
        """
        ...

    @property
    def ElementProperty(self):
        """ Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself. """
        ...

    @property
    def EvaluationContext(self):
        """ Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object. """
        ...

    @property
    def HasContext(self):
        """ Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll. """
        ...

    @property
    def PolicyEnforcement(self):
        """
        Gets or sets the policy enforcement value for this configuration policy element.

        Get: PolicyEnforcement(self: ExtendedProtectionPolicyElement) -> PolicyEnforcement

        Set: PolicyEnforcement(self: ExtendedProtectionPolicyElement) = value
        """
        ...

    @property
    def Properties(self): ...

    @property
    def ProtectionScenario(self):
        """
        Gets or sets the kind of protection enforced by the extended protection policy for this configuration policy element.

        Get: ProtectionScenario(self: ExtendedProtectionPolicyElement) -> ProtectionScenario

        Set: ProtectionScenario(self: ExtendedProtectionPolicyElement) = value
        """
        ...



class ServiceNameElement(ConfigurationElement):
    """
    The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement class represents a configuration element for a service name used in a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.

    ServiceNameElement()
    """
    @property
    def ElementProperty(self):
        """ Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself. """
        ...

    @property
    def EvaluationContext(self):
        """ Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object. """
        ...

    @property
    def HasContext(self):
        """ Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll. """
        ...

    @property
    def Name(self):
        """
        Gets or sets the Service Provider Name (SPN) for this System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance.

        Get: Name(self: ServiceNameElement) -> str

        Set: Name(self: ServiceNameElement) = value
        """
        ...

    @property
    def Properties(self): ...



class ServiceNameElementCollection(ConfigurationElementCollection): # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>
    """
    The System.Security.Authentication.ExtendedProtection.ServiceNameCollection class is a collection of service principal names that represent a configuration element for an System.Security.Authentication.ExtendedProtection.ExtendedProtectionPolicy.

    ServiceNameElementCollection()
    """
    def Add(self, element):
        """
        Add(self: ServiceNameElementCollection, element: ServiceNameElement)

            The 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Add(System.Security.Authentication.ExtendedProtection.Configuration.Service

             NameElement) method adds a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.

            element: The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to add to this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        """
        ...

    def Clear(self):
        """
        Clear(self: ServiceNameElementCollection)

            The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Clear method removes all configuration element objects from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        """
        ...

    def IndexOf(self, element):
        """
        IndexOf(self: ServiceNameElementCollection, element: ServiceNameElement) -> int

            The 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.IndexOf(System.Security.Authentication.ExtendedProtection.Configuration.Ser

             viceNameElement) method retrieves the index of the specified configuration element in this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.

            element: The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to retrieve the index of in this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.

            Returns: The index of the specified System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement in this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        """
        ...

    def Remove(self, *__args):
        """
        Remove(self: ServiceNameElementCollection, element: ServiceNameElement)

            The 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Remove(System.Security.Authentication.ExtendedProtection.Configuration.Serv

             iceNameElement) method removes a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.

            element: The System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to remove from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.

        Remove(self: ServiceNameElementCollection, name: str)

            The 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Remove(System.Security.Authentication.ExtendedProtection.Configuration.Serv

             iceNameElement) method removes a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection based on the System.String specified.

            name: A System.String that represents the System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to remove from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection
        """
        ...

    def RemoveAt(self, index):
        """
        RemoveAt(self: ServiceNameElementCollection, index: int)

            The 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.Remove(System.Security.Authentication.ExtendedProtection.Configuration.Serv

             iceNameElement) method removes a System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection based on the index specified.

            index: The index of the System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElement instance to remove from this 

             System.Security.Authentication.ExtendedProtection.Configuration.ServiceNameElementCollection.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...

    @property
    def AddElementName(self):
        """ Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the add operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class. """
        ...

    @property
    def ClearElementName(self):
        """ Gets or sets the name for the System.Configuration.ConfigurationElement to associate with the clear operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class. """
        ...

    @property
    def ElementName(self):
        """ Gets the name used to identify this collection of elements in the configuration file when overridden in a derived class. """
        ...

    @property
    def ElementProperty(self):
        """ Gets the System.Configuration.ConfigurationElementProperty object that represents the System.Configuration.ConfigurationElement object itself. """
        ...

    @property
    def EvaluationContext(self):
        """ Gets the System.Configuration.ContextInformation object for the System.Configuration.ConfigurationElement object. """
        ...

    @property
    def HasContext(self):
        """ Gets a value that indicates whether the System.Configuration.ConfigurationElement.CurrentConfiguration property is ll. """
        ...

    @property
    def Properties(self):
        """ Gets the collection of properties. """
        ...

    @property
    def RemoveElementName(self):
        """ Gets or sets the name of the System.Configuration.ConfigurationElement to associate with the remove operation in the System.Configuration.ConfigurationElementCollection when overridden in a derived class. """
        ...

    @property
    def ThrowOnDuplicate(self):
        """ Gets a value indicating whether an attempt to add a duplicate System.Configuration.ConfigurationElement to the System.Configuration.ConfigurationElementCollection will cause an exception to be thrown. """
        ...




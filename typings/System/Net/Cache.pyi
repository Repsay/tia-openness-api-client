# encoding: utf-8
# module System.Net.Cache calls itself Cache
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HttpCacheAgeControl(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies the meaning of time values that control caching behavior for resources obtained using System.Net.HttpWebRequest objects.

    enum HttpCacheAgeControl, values: MaxAge (2), MaxAgeAndMaxStale (6), MaxAgeAndMinFresh (3), MaxStale (4), MinFresh (1), None (0)
    """

    MaxAge = None
    MaxAgeAndMaxStale = None
    MaxAgeAndMinFresh = None
    MaxStale = None
    MinFresh = None

    value__ = None

class HttpRequestCacheLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies caching behavior for resources obtained using the Hypertext Transfer protocol (HTTP).

    enum HttpRequestCacheLevel, values: BypassCache (1), CacheIfAvailable (3), CacheOnly (2), CacheOrNextCacheOnly (7), Default (0), NoCacheNoStore (6), Refresh (8), Reload (5), Revalidate (4)
    """

    BypassCache = None
    CacheIfAvailable = None
    CacheOnly = None
    CacheOrNextCacheOnly = None
    Default = None
    NoCacheNoStore = None
    Refresh = None
    Reload = None
    Revalidate = None
    value__ = None

class RequestCachePolicy:  # skipped bases: <type 'object'>
    """
    Defines an application's caching requirements for resources obtained by using System.Net.WebRequest objects.

    RequestCachePolicy()

    RequestCachePolicy(level: RequestCacheLevel)
    """

    def ToString(self):
        """
        ToString(self: RequestCachePolicy) -> str

            Returns a string representation of this instance.

            Returns: A System.String containing the System.Net.Cache.RequestCachePolicy.Level for this instance.
        """
        ...
    @property
    def Level(self):
        """
        Gets the System.Net.Cache.RequestCacheLevel value specified when this instance was constructed.

        Get: Level(self: RequestCachePolicy) -> RequestCacheLevel
        """
        ...

class HttpRequestCachePolicy(RequestCachePolicy):
    """
    Defines an application's caching requirements for resources obtained by using System.Net.HttpWebRequest objects.

    HttpRequestCachePolicy()

    HttpRequestCachePolicy(level: HttpRequestCacheLevel)

    HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: TimeSpan)

    HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan)

    HttpRequestCachePolicy(cacheSyncDate: DateTime)

    HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan, cacheSyncDate: DateTime)
    """

    @property
    def CacheSyncDate(self):
        """
        Gets the cache synchronization date for this instance.

        Get: CacheSyncDate(self: HttpRequestCachePolicy) -> DateTime
        """
        ...
    @property
    def Level(self):
        """
        Gets the System.Net.Cache.HttpRequestCacheLevel value that was specified when this instance was created.

        Get: Level(self: HttpRequestCachePolicy) -> HttpRequestCacheLevel
        """
        ...
    @property
    def MaxAge(self):
        """
        Gets the maximum age permitted for a resource returned from the cache.

        Get: MaxAge(self: HttpRequestCachePolicy) -> TimeSpan
        """
        ...
    @property
    def MaxStale(self):
        """
        Gets the maximum staleness value that is permitted for a resource returned from the cache.

        Get: MaxStale(self: HttpRequestCachePolicy) -> TimeSpan
        """
        ...
    @property
    def MinFresh(self):
        """
        Gets the minimum freshness that is permitted for a resource returned from the cache.

        Get: MinFresh(self: HttpRequestCachePolicy) -> TimeSpan
        """
        ...

class RequestCacheLevel(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Specifies caching behavior for resources obtained using System.Net.WebRequest and its derived classes.

    enum RequestCacheLevel, values: BypassCache (1), CacheIfAvailable (3), CacheOnly (2), Default (0), NoCacheNoStore (6), Reload (5), Revalidate (4)
    """

    BypassCache = None
    CacheIfAvailable = None
    CacheOnly = None
    Default = None
    NoCacheNoStore = None
    Reload = None
    Revalidate = None
    value__ = None

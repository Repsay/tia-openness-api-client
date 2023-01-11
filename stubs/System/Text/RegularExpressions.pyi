# encoding: utf-8
# module System.Text.RegularExpressions calls itself RegularExpressions
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Capture:  # skipped bases: <type 'object'>
    """Represents the results from a single successful subexpression capture."""

    def ToString(self):
        """
        ToString(self: Capture) -> str

            Retrieves the captured substring from the input string by calling the System.Text.RegularExpressions.Capture.Value property.

            Returns: The substring that was captured by the match.
        """
        ...
    @property
    def Index(self):
        """
        The position in the original string where the first character of the captured substring is found.

        Get: Index(self: Capture) -> int
        """
        ...
    @property
    def Length(self):
        """
        Gets the length of the captured substring.

        Get: Length(self: Capture) -> int
        """
        ...
    @property
    def Value(self):
        """
        Gets the captured substring from the input string.

        Get: Value(self: Capture) -> str
        """
        ...

class CaptureCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents the set of captures made by a single capturing group."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: CaptureCollection) -> IEnumerator

            Provides an enumerator that iterates through the collection.

            Returns: An object that contains all System.Text.RegularExpressions.Capture objects within the System.Text.RegularExpressions.CaptureCollection.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of substrings captured by the group.

        Get: Count(self: CaptureCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether the collection is read only.

        Get: IsReadOnly(self: CaptureCollection) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value that indicates whether access to the collection is synchronized (thread-safe).

        Get: IsSynchronized(self: CaptureCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the collection.

        Get: SyncRoot(self: CaptureCollection) -> object
        """
        ...

class Group(Capture):
    """Represents the results from a single capturing group."""

    @staticmethod
    def Synchronized(inner):
        """
        Synchronized(inner: Group) -> Group

            Returns a oup object equivalent to the one supplied that is safe to share between multiple threads.

            inner: The input System.Text.RegularExpressions.Group object.

            Returns: A regular expression oup object.
        """
        ...
    @property
    def Captures(self):
        """
        Gets a collection of all the captures matched by the capturing group, in innermost-leftmost-first order (or innermost-rightmost-first order if the regular expression is modified with the System.Text.RegularExpressions.RegexOptions.RightToLeft option). The collection may have zero or more items.

        Get: Captures(self: Group) -> CaptureCollection
        """
        ...
    @property
    def Name(self):
        """
        Returns the name of the capturing group representing by the current instance.

        Get: Name(self: Group) -> str
        """
        ...
    @property
    def Success(self):
        """
        Gets a value indicating whether the match is successful.

        Get: Success(self: Group) -> bool
        """
        ...

class GroupCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Returns the set of captured groups in a single match."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: GroupCollection) -> IEnumerator

            Provides an enumerator that iterates through the collection.

            Returns: An enumerator that contains all System.Text.RegularExpressions.Group objects in the System.Text.RegularExpressions.GroupCollection.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Returns the number of groups in the collection.

        Get: Count(self: GroupCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether the collection is read-only.

        Get: IsReadOnly(self: GroupCollection) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value that indicates whether access to the System.Text.RegularExpressions.GroupCollection is synchronized (thread-safe).

        Get: IsSynchronized(self: GroupCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the System.Text.RegularExpressions.GroupCollection.

        Get: SyncRoot(self: GroupCollection) -> object
        """
        ...

class Match(Group):
    """Represents the results from a single regular expression match."""

    def NextMatch(self):
        """
        NextMatch(self: Match) -> Match

            Returns a new System.Text.RegularExpressions.Match object with the results for the next match, starting at the position at which the last match ended (at the character after the last matched character).

            Returns: The next regular expression match.
        """
        ...
    def Result(self, replacement):
        """
        Result(self: Match, replacement: str) -> str

            Returns the expansion of the specified replacement pattern.

            replacement: The replacement pattern to use.

            Returns: The expanded version of the replacement parameter.
        """
        ...
    @property
    def Groups(self):
        """
        Gets a collection of groups matched by the regular expression.

        Get: Groups(self: Match) -> GroupCollection
        """
        ...
    Empty = None

class MatchCollection(object, ICollection):  # skipped bases: <type 'IEnumerable'>
    """Represents the set of successful matches found by iteratively applying a regular expression pattern to the input string."""

    def GetEnumerator(self):
        """
        GetEnumerator(self: MatchCollection) -> IEnumerator

            Provides an enumerator that iterates through the collection.

            Returns: An object that contains all System.Text.RegularExpressions.Match objects within the System.Text.RegularExpressions.MatchCollection.
        """
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def Count(self):
        """
        Gets the number of matches.

        Get: Count(self: MatchCollection) -> int
        """
        ...
    @property
    def IsReadOnly(self):
        """
        Gets a value that indicates whether the collection is read only.

        Get: IsReadOnly(self: MatchCollection) -> bool
        """
        ...
    @property
    def IsSynchronized(self):
        """
        Gets a value indicating whether access to the collection is synchronized (thread-safe).

        Get: IsSynchronized(self: MatchCollection) -> bool
        """
        ...
    @property
    def SyncRoot(self):
        """
        Gets an object that can be used to synchronize access to the collection.

        Get: SyncRoot(self: MatchCollection) -> object
        """
        ...

class MatchEvaluator(MulticastDelegate):  # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>
    """
    Represents the method that is called each time a regular expression match is found during a erload:System.Text.RegularExpressions.Regex.Replace method operation.

    MatchEvaluator(object: object, method: IntPtr)
    """

    def BeginInvoke(self, match, callback, object):
        """BeginInvoke(self: MatchEvaluator, match: Match, callback: AsyncCallback, object: object) -> IAsyncResult"""
        ...
    def EndInvoke(self, result):
        """EndInvoke(self: MatchEvaluator, result: IAsyncResult) -> str"""
        ...
    def Invoke(self, match):
        """Invoke(self: MatchEvaluator, match: Match) -> str"""
        ...

class Regex(object, ISerializable):
    """
    Represents an immutable regular expression.To browse the .NET Framework source code for this type, see the Reference Source.

    Regex(pattern: str)

    Regex(pattern: str, options: RegexOptions)

    Regex(pattern: str, options: RegexOptions, matchTimeout: TimeSpan)
    """

    @staticmethod
    def CompileToAssembly(regexinfos, assemblyname, attributes=None, resourceFile=None):
        """
        CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName)

            Compiles one or more specified System.Text.RegularExpressions.Regex objects to a named assembly.

            regexinfos: An array that describes the regular expressions to compile.

            assemblyname: The file name of the assembly.

        CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName, attributes: Array[CustomAttributeBuilder])

            Compiles one or more specified System.Text.RegularExpressions.Regex objects to a named assembly with the specified attributes.

            regexinfos: An array that describes the regular expressions to compile.

            assemblyname: The file name of the assembly.

            attributes: An array that defines the attributes to apply to the assembly.

        CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName, attributes: Array[CustomAttributeBuilder], resourceFile: str)

            Compiles one or more specified System.Text.RegularExpressions.Regex objects and a specified resource file to a named assembly with the specified attributes.

            regexinfos: An array that describes the regular expressions to compile.

            assemblyname: The file name of the assembly.

            attributes: An array that defines the attributes to apply to the assembly.

            resourceFile: The name of the Win32 resource file to include in the assembly.
        """
        ...
    @staticmethod
    def Escape(str):
        """
        Escape(str: str) -> str

            Escapes a minimal set of characters (\, *, +, ?, |, {, [, (,), ^, $,., #, and white space) by replacing them with their escape codes. This instructs the regular expression engine to interpret these characters literally rather than

             as metacharacters.

            str: The input string that contains the text to convert.

            Returns: A string of characters with metacharacters converted to their escaped form.
        """
        ...
    def GetGroupNames(self):
        """
        GetGroupNames(self: Regex) -> Array[str]

            Returns an array of capturing group names for the regular expression.

            Returns: A string array of group names.
        """
        ...
    def GetGroupNumbers(self):
        """
        GetGroupNumbers(self: Regex) -> Array[int]

            Returns an array of capturing group numbers that correspond to group names in an array.

            Returns: An integer array of group numbers.
        """
        ...
    def GroupNameFromNumber(self, i):
        """
        GroupNameFromNumber(self: Regex, i: int) -> str

            Gets the group name that corresponds to the specified group number.

            i: The group number to convert to the corresponding group name.

            Returns: A string that contains the group name associated with the specified group number. If there is no group name that corresponds to i, the method returns System.String.Empty.
        """
        ...
    def GroupNumberFromName(self, name):
        """
        GroupNumberFromName(self: Regex, name: str) -> int

            Returns the group number that corresponds to the specified group name.

            name: The group name to convert to the corresponding group number.

            Returns: The group number that corresponds to the specified group name, or -1 if name is not a valid group name.
        """
        ...
    def InitializeReferences(self, *args):  # cannot find CLR method
        """
        InitializeReferences(self: Regex)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    @staticmethod
    def IsMatch(input, *__args):
        """
        IsMatch(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> bool

            Indicates whether the specified regular expression finds a match in the specified input string, using the specified matching options and time-out interval.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that provide options for matching.

            matchTimeout: A time-out interval, or System.Text.RegularExpressions.Regex.InfiniteMatchTimeout to indicate that the method should not time out.

            Returns: ue if the regular expression finds a match; otherwise, lse.

        IsMatch(self: Regex, input: str) -> bool

            Indicates whether the regular expression specified in the System.Text.RegularExpressions.Regex constructor finds a match in a specified input string.

            input: The string to search for a match.

            Returns: ue if the regular expression finds a match; otherwise, lse.

        IsMatch(self: Regex, input: str, startat: int) -> bool

            Indicates whether the regular expression specified in the System.Text.RegularExpressions.Regex constructor finds a match in the specified input string, beginning at the specified starting position in the string.

            input: The string to search for a match.

            startat: The character position at which to start the search.

            Returns: ue if the regular expression finds a match; otherwise, lse.

        IsMatch(input: str, pattern: str) -> bool

            Indicates whether the specified regular expression finds a match in the specified input string.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            Returns: ue if the regular expression finds a match; otherwise, lse.

        IsMatch(input: str, pattern: str, options: RegexOptions) -> bool

            Indicates whether the specified regular expression finds a match in the specified input string, using the specified matching options.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that provide options for matching.

            Returns: ue if the regular expression finds a match; otherwise, lse.
        """
        ...
    @staticmethod
    def Match(input, *__args):
        """
        Match(input: str, pattern: str, options: RegexOptions) -> Match

            Searches the input string for the first occurrence of the specified regular expression, using the specified matching options.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that provide options for matching.

            Returns: An object that contains information about the match.

        Match(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> Match

            Searches the input string for the first occurrence of the specified regular expression, using the specified matching options and time-out interval.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that provide options for matching.

            matchTimeout: A time-out interval, or System.Text.RegularExpressions.Regex.InfiniteMatchTimeout to indicate that the method should not time out.

            Returns: An object that contains information about the match.

        Match(self: Regex, input: str) -> Match

            Searches the specified input string for the first occurrence of the regular expression specified in the System.Text.RegularExpressions.Regex constructor.

            input: The string to search for a match.

            Returns: An object that contains information about the match.

        Match(self: Regex, input: str, startat: int) -> Match

            Searches the input string for the first occurrence of a regular expression, beginning at the specified starting position in the string.

            input: The string to search for a match.

            startat: The zero-based character position at which to start the search.

            Returns: An object that contains information about the match.

        Match(self: Regex, input: str, beginning: int, length: int) -> Match

            Searches the input string for the first occurrence of a regular expression, beginning at the specified starting position and searching only the specified number of characters.

            input: The string to search for a match.

            beginning: The zero-based character position in the input string that defines the leftmost position to be searched.

            length: The number of characters in the substring to include in the search.

            Returns: An object that contains information about the match.

        Match(input: str, pattern: str) -> Match

            Searches the specified input string for the first occurrence of the specified regular expression.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            Returns: An object that contains information about the match.
        """
        ...
    @staticmethod
    def Matches(input, *__args):
        """
        Matches(input: str, pattern: str) -> MatchCollection

            Searches the specified input string for all occurrences of a specified regular expression.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no matches are found, the method returns an empty collection object.

        Matches(input: str, pattern: str, options: RegexOptions) -> MatchCollection

            Searches the specified input string for all occurrences of a specified regular expression, using the specified matching options.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that specify options for matching.

            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no matches are found, the method returns an empty collection object.

        Matches(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> MatchCollection

            Searches the specified input string for all occurrences of a specified regular expression, using the specified matching options and time-out interval.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that specify options for matching.

            matchTimeout: A time-out interval, or System.Text.RegularExpressions.Regex.InfiniteMatchTimeout to indicate that the method should not time out.

            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no matches are found, the method returns an empty collection object.

        Matches(self: Regex, input: str) -> MatchCollection

            Searches the specified input string for all occurrences of a regular expression.

            input: The string to search for a match.

            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no matches are found, the method returns an empty collection object.

        Matches(self: Regex, input: str, startat: int) -> MatchCollection

            Searches the specified input string for all occurrences of a regular expression, beginning at the specified starting position in the string.

            input: The string to search for a match.

            startat: The character position in the input string at which to start the search.

            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no matches are found, the method returns an empty collection object.
        """
        ...
    @staticmethod
    def Replace(input, *__args):
        """
        Replace(input: str, pattern: str, replacement: str) -> str

            In a specified input string, replaces all strings that match a specified regular expression with a specified replacement string.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            replacement: The replacement string.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If pattern is not matched in the current instance, the method returns the current instance unchanged.

        Replace(input: str, pattern: str, replacement: str, options: RegexOptions) -> str

            In a specified input string, replaces all strings that match a specified regular expression with a specified replacement string. Specified options modify the matching operation.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            replacement: The replacement string.

            options: A bitwise combination of the enumeration values that provide options for matching.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If pattern is not matched in the current instance, the method returns the current instance unchanged.

        Replace(input: str, pattern: str, replacement: str, options: RegexOptions, matchTimeout: TimeSpan) -> str

            In a specified input string, replaces all strings that match a specified regular expression with a specified replacement string. Additional parameters specify options that modify the matching operation and a time-out interval if no

             match is found.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            replacement: The replacement string.

            options: A bitwise combination of the enumeration values that provide options for matching.

            matchTimeout: A time-out interval, or System.Text.RegularExpressions.Regex.InfiniteMatchTimeout to indicate that the method should not time out.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If pattern is not matched in the current instance, the method returns the current instance unchanged.

        Replace(self: Regex, input: str, replacement: str) -> str

            In a specified input string, replaces all strings that match a regular expression pattern with a specified replacement string.

            input: The string to search for a match.

            replacement: The replacement string.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If the regular expression pattern is not matched in the current instance, the method returns the current

             instance unchanged.

        Replace(self: Regex, input: str, replacement: str, count: int) -> str

            In a specified input string, replaces a specified maximum number of strings that match a regular expression pattern with a specified replacement string.

            input: The string to search for a match.

            replacement: The replacement string.

            count: The maximum number of times the replacement can occur.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If the regular expression pattern is not matched in the current instance, the method returns the current

             instance unchanged.

        Replace(self: Regex, input: str, replacement: str, count: int, startat: int) -> str

            In a specified input substring, replaces a specified maximum number of strings that match a regular expression pattern with a specified replacement string.

            input: The string to search for a match.

            replacement: The replacement string.

            count: Maximum number of times the replacement can occur.

            startat: The character position in the input string where the search begins.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If the regular expression pattern is not matched in the current instance, the method returns the current

             instance unchanged.

        Replace(input: str, pattern: str, evaluator: MatchEvaluator) -> str

            In a specified input string, replaces all strings that match a specified regular expression with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            evaluator: A custom method that examines each match and returns either the original matched string or a replacement string.

            Returns: A new string that is identical to the input string, except that a replacement string takes the place of each matched string. If pattern is not matched in the current instance, the method returns the current instance unchanged.

        Replace(input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions) -> str

            In a specified input string, replaces all strings that match a specified regular expression with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate. Specified options modify the matching operation.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            evaluator: A custom method that examines each match and returns either the original matched string or a replacement string.

            options: A bitwise combination of the enumeration values that provide options for matching.

            Returns: A new string that is identical to the input string, except that a replacement string takes the place of each matched string. If pattern is not matched in the current instance, the method returns the current instance unchanged.

        Replace(input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions, matchTimeout: TimeSpan) -> str

            In a specified input string, replaces all substrings that match a specified regular expression with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate. Additional parameters specify options that modify the

             matching operation and a time-out interval if no match is found.

            input: The string to search for a match.

            pattern: The regular expression pattern to match.

            evaluator: A custom method that examines each match and returns either the original matched string or a replacement string.

            options: A bitwise combination of enumeration values that provide options for matching.

            matchTimeout: A time-out interval, or System.Text.RegularExpressions.Regex.InfiniteMatchTimeout to indicate that the method should not time out.

            Returns: A new string that is identical to the input string, except that the replacement string takes the place of each matched string. If pattern is not matched in the current instance, the method returns the current instance unchanged.

        Replace(self: Regex, input: str, evaluator: MatchEvaluator) -> str

            In a specified input string, replaces all strings that match a specified regular expression with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate.

            input: The string to search for a match.

            evaluator: A custom method that examines each match and returns either the original matched string or a replacement string.

            Returns: A new string that is identical to the input string, except that a replacement string takes the place of each matched string. If the regular expression pattern is not matched in the current instance, the method returns the current

             instance unchanged.

        Replace(self: Regex, input: str, evaluator: MatchEvaluator, count: int) -> str

            In a specified input string, replaces a specified maximum number of strings that match a regular expression pattern with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate.

            input: The string to search for a match.

            evaluator: A custom method that examines each match and returns either the original matched string or a replacement string.

            count: The maximum number of times the replacement will occur.

            Returns: A new string that is identical to the input string, except that a replacement string takes the place of each matched string. If the regular expression pattern is not matched in the current instance, the method returns the current

             instance unchanged.

        Replace(self: Regex, input: str, evaluator: MatchEvaluator, count: int, startat: int) -> str

            In a specified input substring, replaces a specified maximum number of strings that match a regular expression pattern with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate.

            input: The string to search for a match.

            evaluator: A custom method that examines each match and returns either the original matched string or a replacement string.

            count: The maximum number of times the replacement will occur.

            startat: The character position in the input string where the search begins.

            Returns: A new string that is identical to the input string, except that a replacement string takes the place of each matched string. If the regular expression pattern is not matched in the current instance, the method returns the current

             instance unchanged.
        """
        ...
    @staticmethod
    def Split(input, *__args):
        """
        Split(input: str, pattern: str) -> Array[str]

            Splits an input string into an array of substrings at the positions defined by a regular expression pattern.

            input: The string to split.

            pattern: The regular expression pattern to match.

            Returns: An array of strings.

        Split(input: str, pattern: str, options: RegexOptions) -> Array[str]

            Splits an input string into an array of substrings at the positions defined by a specified regular expression pattern. Specified options modify the matching operation.

            input: The string to split.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that provide options for matching.

            Returns: An array of strings.

        Split(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> Array[str]

            Splits an input string into an array of substrings at the positions defined by a specified regular expression pattern. Additional parameters specify options that modify the matching operation and a time-out interval if no match is

             found.

            input: The string to split.

            pattern: The regular expression pattern to match.

            options: A bitwise combination of the enumeration values that provide options for matching.

            matchTimeout: A time-out interval, or System.Text.RegularExpressions.Regex.InfiniteMatchTimeout to indicate that the method should not time out.

            Returns: A string array.

        Split(self: Regex, input: str) -> Array[str]

            Splits an input string into an array of substrings at the positions defined by a regular expression pattern specified in the System.Text.RegularExpressions.Regex constructor.

            input: The string to split.

            Returns: An array of strings.

        Split(self: Regex, input: str, count: int) -> Array[str]

            Splits an input string a specified maximum number of times into an array of substrings, at the positions defined by a regular expression specified in the System.Text.RegularExpressions.Regex constructor.

            input: The string to be split.

            count: The maximum number of times the split can occur.

            Returns: An array of strings.

        Split(self: Regex, input: str, count: int, startat: int) -> Array[str]

            Splits an input string a specified maximum number of times into an array of substrings, at the positions defined by a regular expression specified in the System.Text.RegularExpressions.Regex constructor. The search for the regular

             expression pattern starts at a specified character position in the input string.

            input: The string to be split.

            count: The maximum number of times the split can occur.

            startat: The character position in the input string where the search will begin.

            Returns: An array of strings.
        """
        ...
    def ToString(self):
        """
        ToString(self: Regex) -> str

            Returns the regular expression pattern that was passed into the gex constructor.

            Returns: The pattern parameter that was passed into the gex constructor.
        """
        ...
    @staticmethod
    def Unescape(str):
        """
        Unescape(str: str) -> str

            Converts any escaped characters in the input string.

            str: The input string containing the text to convert.

            Returns: A string of characters with any escaped characters converted to their unescaped form.
        """
        ...
    def UseOptionC(self, *args):  # cannot find CLR method
        """
        UseOptionC(self: Regex) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            Returns: ue if the System.Text.RegularExpressions.Regex.Options property contains the System.Text.RegularExpressions.RegexOptions.Compiled option; otherwise, lse.
        """
        ...
    def UseOptionR(self, *args):  # cannot find CLR method
        """
        UseOptionR(self: Regex) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            Returns: ue if the System.Text.RegularExpressions.Regex.Options property contains the System.Text.RegularExpressions.RegexOptions.RightToLeft option; otherwise, lse.
        """
        ...
    def ValidateMatchTimeout(self, *args):  # cannot find CLR method
        """
        ValidateMatchTimeout(matchTimeout: TimeSpan)

            Checks whether a time-out interval is within an acceptable range.

            matchTimeout: The time-out interval to check.
        """
        ...
    @property
    def CapNames(self):
        """Gets or sets a dictionary that maps named capturing groups to their index values."""
        ...
    @property
    def Caps(self):
        """Gets or sets a dictionary that maps numbered capturing groups to their index values."""
        ...
    @property
    def MatchTimeout(self):
        """
        Gets the time-out interval of the current instance.

        Get: MatchTimeout(self: Regex) -> TimeSpan
        """
        ...
    @property
    def Options(self):
        """
        Gets the options that were passed into the System.Text.RegularExpressions.Regex constructor.

        Get: Options(self: Regex) -> RegexOptions
        """
        ...
    @property
    def RightToLeft(self):
        """
        Gets a value that indicates whether the regular expression searches from right to left.

        Get: RightToLeft(self: Regex) -> bool
        """
        ...
    CacheSize = 15
    capnames = None
    caps = None
    capsize = None
    capslist = None
    factory = None
    InfiniteMatchTimeout = None
    internalMatchTimeout = None
    pattern = None
    roptions = None

class RegexCompilationInfo:  # skipped bases: <type 'object'>
    """
    Provides information about a regular expression that is used to compile a regular expression to a stand-alone assembly.

    RegexCompilationInfo(pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool)

    RegexCompilationInfo(pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool, matchTimeout: TimeSpan)
    """

    @property
    def IsPublic(self):
        """
        Gets or sets a value that indicates whether the compiled regular expression has public visibility.

        Get: IsPublic(self: RegexCompilationInfo) -> bool

        Set: IsPublic(self: RegexCompilationInfo) = value
        """
        ...
    @property
    def MatchTimeout(self):
        """
        Gets or sets the regular expression's default time-out interval.

        Get: MatchTimeout(self: RegexCompilationInfo) -> TimeSpan

        Set: MatchTimeout(self: RegexCompilationInfo) = value
        """
        ...
    @property
    def Name(self):
        """
        Gets or sets the name of the type that represents the compiled regular expression.

        Get: Name(self: RegexCompilationInfo) -> str

        Set: Name(self: RegexCompilationInfo) = value
        """
        ...
    @property
    def Namespace(self):
        """
        Gets or sets the namespace to which the new type belongs.

        Get: Namespace(self: RegexCompilationInfo) -> str

        Set: Namespace(self: RegexCompilationInfo) = value
        """
        ...
    @property
    def Options(self):
        """
        Gets or sets the options to use when compiling the regular expression.

        Get: Options(self: RegexCompilationInfo) -> RegexOptions

        Set: Options(self: RegexCompilationInfo) = value
        """
        ...
    @property
    def Pattern(self):
        """
        Gets or sets the regular expression to compile.

        Get: Pattern(self: RegexCompilationInfo) -> str

        Set: Pattern(self: RegexCompilationInfo) = value
        """
        ...

class RegexMatchTimeoutException(TimeoutException):  # skipped bases: <type '_Exception'>, <type 'ISerializable'>
    """
    The exception that is thrown when the execution time of a regular expression pattern-matching method exceeds its time-out interval.

    RegexMatchTimeoutException(regexInput: str, regexPattern: str, matchTimeout: TimeSpan)

    RegexMatchTimeoutException()

    RegexMatchTimeoutException(message: str)

    RegexMatchTimeoutException(message: str, inner: Exception)
    """

    @property
    def Input(self):
        """
        Gets the input text that the regular expression engine was processing when the time-out occurred.

        Get: Input(self: RegexMatchTimeoutException) -> str
        """
        ...
    @property
    def MatchTimeout(self):
        """
        Gets the time-out interval for a regular expression match.

        Get: MatchTimeout(self: RegexMatchTimeoutException) -> TimeSpan
        """
        ...
    @property
    def Pattern(self):
        """
        Gets the regular expression pattern that was used in the matching operation when the time-out occurred.

        Get: Pattern(self: RegexMatchTimeoutException) -> str
        """
        ...
    SerializeObjectState = None

class RegexOptions(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Provides enumerated values to use to set regular expression options.

    enum (flags) RegexOptions, values: Compiled (8), CultureInvariant (512), ECMAScript (256), ExplicitCapture (4), IgnoreCase (1), IgnorePatternWhitespace (32), Multiline (2), None (0), RightToLeft (64), Singleline (16)
    """

    Compiled = None
    CultureInvariant = None
    ECMAScript = None
    ExplicitCapture = None
    IgnoreCase = None
    IgnorePatternWhitespace = None
    Multiline = None

    RightToLeft = None
    Singleline = None
    value__ = None

class RegexRunner:  # skipped bases: <type 'object'>
    """The System.Text.RegularExpressions.RegexRunner class is the base class for compiled regular expressions."""

    def Capture(self, *args):  # cannot find CLR method
        """
        Capture(self: RegexRunner, capnum: int, start: int, end: int)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            capnum: A capture number.

            start: The starting position of the capture.

            end: The ending position of the capture.
        """
        ...
    def CharInClass(self, *args):  # cannot find CLR method
        """
        CharInClass(ch: Char, charClass: str) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method. Determines whether a character is in a character class.

            ch: A character to test.

            charClass: The internal name of a character class.

            Returns: ue if the ch parameter is in the character class specified by the charClass parameter.
        """
        ...
    def CharInSet(self, *args):  # cannot find CLR method
        """
        CharInSet(ch: Char, set: str, category: str) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            ch: A character.

            set: The character set.

            category: The character category.

            Returns: Returns System.Boolean.
        """
        ...
    def CheckTimeout(self, *args):  # cannot find CLR method
        """
        CheckTimeout(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def Crawl(self, *args):  # cannot find CLR method
        """
        Crawl(self: RegexRunner, i: int)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            i: A number to save.
        """
        ...
    def Crawlpos(self, *args):  # cannot find CLR method
        """
        Crawlpos(self: RegexRunner) -> int

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            Returns: Returns System.Int32.
        """
        ...
    def DoubleCrawl(self, *args):  # cannot find CLR method
        """
        DoubleCrawl(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def DoubleStack(self, *args):  # cannot find CLR method
        """
        DoubleStack(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def DoubleTrack(self, *args):  # cannot find CLR method
        """
        DoubleTrack(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def EnsureStorage(self, *args):  # cannot find CLR method
        """
        EnsureStorage(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def FindFirstChar(self, *args):  # cannot find CLR method
        """
        FindFirstChar(self: RegexRunner) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            Returns: Returns System.Boolean.
        """
        ...
    def Go(self, *args):  # cannot find CLR method
        """
        Go(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def InitTrackCount(self, *args):  # cannot find CLR method
        """
        InitTrackCount(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    def IsBoundary(self, *args):  # cannot find CLR method
        """
        IsBoundary(self: RegexRunner, index: int, startpos: int, endpos: int) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            index: The possible boundary position.

            startpos: The starting position.

            endpos: The ending position.

            Returns: Returns System.Boolean.
        """
        ...
    def IsECMABoundary(self, *args):  # cannot find CLR method
        """
        IsECMABoundary(self: RegexRunner, index: int, startpos: int, endpos: int) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            index: The possible ECMA boundary position.

            startpos: The starting position.

            endpos: The ending position.

            Returns: Returns System.Boolean.
        """
        ...
    def IsMatched(self, *args):  # cannot find CLR method
        """
        IsMatched(self: RegexRunner, cap: int) -> bool

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            cap: The capture number.

            Returns: Returns System.Boolean.
        """
        ...
    def MatchIndex(self, *args):  # cannot find CLR method
        """
        MatchIndex(self: RegexRunner, cap: int) -> int

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            cap: The capture number.

            Returns: Returns System.Int32.
        """
        ...
    def MatchLength(self, *args):  # cannot find CLR method
        """
        MatchLength(self: RegexRunner, cap: int) -> int

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            cap: The capture number.

            Returns: Returns System.Int32.
        """
        ...
    def Popcrawl(self, *args):  # cannot find CLR method
        """
        Popcrawl(self: RegexRunner) -> int

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            Returns: Returns System.Int32.
        """
        ...
    def Scan(self, *args):  # cannot find CLR method
        """
        Scan(self: RegexRunner, regex: Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool) -> Match

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            regex: An instance of the regular expression engine.

            text: The text to scan for a pattern match.

            textbeg: The zero-based starting position in text at which the regular expression engine scans for a match.

            textend: The zero-based ending position in text at which the regular expression engine scans for a match.

            textstart: The zero-based starting position to scan for this match.

            prevlen: The number of characters in the previous match.

            quick: ue to search for a match in quick mode; otherwise, lse.

            Returns: A match.

        Scan(self: RegexRunner, regex: Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool, timeout: TimeSpan) -> Match

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            regex: An instance of the regular expression engine.

            text: The text to scan for a pattern match.

            textbeg: The zero-based starting position in text at which the regular expression engine scans for a match.

            textend: The zero-based ending position in text at which the regular expression engine scans for a match.

            textstart: The zero-based starting position to scan for this match.

            prevlen: The number of characters in the previous match.

            quick: ue to search for a match in quick mode; otherwise, lse.

            timeout: The timeout interval.

            Returns: A match.
        """
        ...
    def TransferCapture(self, *args):  # cannot find CLR method
        """
        TransferCapture(self: RegexRunner, capnum: int, uncapnum: int, start: int, end: int)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.

            capnum: A capture number.

            uncapnum: A saved capture number.

            start: The starting position.

            end: The ending position.
        """
        ...
    def Uncapture(self, *args):  # cannot find CLR method
        """
        Uncapture(self: RegexRunner)

            Used by a System.Text.RegularExpressions.Regex object generated by the erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        ...
    runcrawl = None
    runcrawlpos = None
    runmatch = None
    runregex = None
    runstack = None
    runstackpos = None
    runtext = None
    runtextbeg = None
    runtextend = None
    runtextpos = None
    runtextstart = None
    runtrack = None
    runtrackcount = None
    runtrackpos = None

class RegexRunnerFactory:  # skipped bases: <type 'object'>
    """Creates a System.Text.RegularExpressions.RegexRunner class for a compiled regular expression."""

    def CreateInstance(self, *args):  # cannot find CLR method
        """
        CreateInstance(self: RegexRunnerFactory) -> RegexRunner

            When overridden in a derived class, creates a System.Text.RegularExpressions.RegexRunner object for a specific compiled regular expression.

            Returns: A System.Text.RegularExpressions.RegexRunner object designed to execute a specific compiled regular expression.
        """
        ...

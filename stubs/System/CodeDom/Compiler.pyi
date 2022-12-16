# encoding: utf-8
# module System.CodeDom.Compiler calls itself Compiler
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

from System.ComponentModel import Component

from System.Collections import CollectionBase, ICollection
from System import Attribute, Enum, IDisposable

from System.IO import TextWriter

class ICodeGenerator:
    """Defines an interface for generating code."""

    def CreateEscapedIdentifier(self, value):
        """
        CreateEscapedIdentifier(self: ICodeGenerator, value: str) -> str

            Creates an escaped identifier for the specified value.

            value: The string to create an escaped identifier for.

            Returns: The escaped identifier for the value.
        """
        ...
    def CreateValidIdentifier(self, value):
        """
        CreateValidIdentifier(self: ICodeGenerator, value: str) -> str

            Creates a valid identifier for the specified value.

            value: The string to generate a valid identifier for.

            Returns: A valid identifier for the specified value.
        """
        ...
    def GenerateCodeFromCompileUnit(self, e, w, o):
        """
        GenerateCodeFromCompileUnit(self: ICodeGenerator, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) compilation unit and outputs it to the specified text writer using the specified options.

            e: A System.CodeDom.CodeCompileUnit to generate code for.

            w: The System.IO.TextWriter to output code to.

            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromExpression(self, e, w, o):
        """
        GenerateCodeFromExpression(self: ICodeGenerator, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) expression and outputs it to the specified text writer.

            e: A System.CodeDom.CodeExpression that indicates the expression to generate code for.

            w: The System.IO.TextWriter to output code to.

            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromNamespace(self, e, w, o):
        """
        GenerateCodeFromNamespace(self: ICodeGenerator, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) namespace and outputs it to the specified text writer using the specified options.

            e: A System.CodeDom.CodeNamespace that indicates the namespace to generate code for.

            w: The System.IO.TextWriter to output code to.

            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromStatement(self, e, w, o):
        """
        GenerateCodeFromStatement(self: ICodeGenerator, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) statement and outputs it to the specified text writer using the specified options.

            e: A System.CodeDom.CodeStatement containing the CodeDOM elements to translate.

            w: The System.IO.TextWriter to output code to.

            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromType(self, e, w, o):
        """
        GenerateCodeFromType(self: ICodeGenerator, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) type declaration and outputs it to the specified text writer using the specified options.

            e: A System.CodeDom.CodeTypeDeclaration that indicates the type to generate code for.

            w: The System.IO.TextWriter to output code to.

            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GetTypeOutput(self, type):
        """
        GetTypeOutput(self: ICodeGenerator, type: CodeTypeReference) -> str

            Gets the type indicated by the specified System.CodeDom.CodeTypeReference.

            type: A System.CodeDom.CodeTypeReference that indicates the type to return.

            Returns: A text representation of the specified type for the language this code generator is designed to generate code in. For example, in Visual Basic, passing in type System.Int32 will return "Integer".
        """
        ...
    def IsValidIdentifier(self, value):
        """
        IsValidIdentifier(self: ICodeGenerator, value: str) -> bool

            Gets a value that indicates whether the specified value is a valid identifier for the current language.

            value: The value to test for being a valid identifier.

            Returns: ue if the value parameter is a valid identifier; otherwise, lse.
        """
        ...
    def Supports(self, supports):
        """
        Supports(self: ICodeGenerator, supports: GeneratorSupport) -> bool

            Gets a value indicating whether the generator provides support for the language features represented by the specified System.CodeDom.Compiler.GeneratorSupport object.

            supports: The capabilities to test the generator for.

            Returns: ue if the specified capabilities are supported; otherwise, lse.
        """
        ...
    def ValidateIdentifier(self, value):
        """
        ValidateIdentifier(self: ICodeGenerator, value: str)

            Throws an exception if the specified value is not a valid identifier.

            value: The identifier to validate.
        """
        ...

class CodeGenerator(ICodeGenerator):
    """Provides an example implementation of the System.CodeDom.Compiler.ICodeGenerator interface. This class is abstract."""

    def ContinueOnNewLine(self, *args):  # cannot find CLR method
        """
        ContinueOnNewLine(self: CodeGenerator, st: str)

            Generates a line-continuation character and outputs the specified string on a new line.

            st: The string to write on the new line.
        """
        ...
    def GenerateArgumentReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateArgumentReferenceExpression(self: CodeGenerator, e: CodeArgumentReferenceExpression)

            Generates code for the specified argument reference expression.

            e: A System.CodeDom.CodeArgumentReferenceExpression that indicates the expression to generate code for.
        """
        ...
    def GenerateArrayCreateExpression(self, *args):  # cannot find CLR method
        """
        GenerateArrayCreateExpression(self: CodeGenerator, e: CodeArrayCreateExpression)

            Generates code for the specified array creation expression.

            e: A System.CodeDom.CodeArrayCreateExpression that indicates the expression to generate code for.
        """
        ...
    def GenerateArrayIndexerExpression(self, *args):  # cannot find CLR method
        """
        GenerateArrayIndexerExpression(self: CodeGenerator, e: CodeArrayIndexerExpression)

            Generates code for the specified array indexer expression.

            e: A System.CodeDom.CodeArrayIndexerExpression that indicates the expression to generate code for.
        """
        ...
    def GenerateAssignStatement(self, *args):  # cannot find CLR method
        """
        GenerateAssignStatement(self: CodeGenerator, e: CodeAssignStatement)

            Generates code for the specified assignment statement.

            e: A System.CodeDom.CodeAssignStatement that indicates the statement to generate code for.
        """
        ...
    def GenerateAttachEventStatement(self, *args):  # cannot find CLR method
        """
        GenerateAttachEventStatement(self: CodeGenerator, e: CodeAttachEventStatement)

            Generates code for the specified attach event statement.

            e: A System.CodeDom.CodeAttachEventStatement that indicates the statement to generate code for.
        """
        ...
    def GenerateAttributeDeclarationsEnd(self, *args):  # cannot find CLR method
        """
        GenerateAttributeDeclarationsEnd(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)

            Generates code for the specified attribute block end.

            attributes: A System.CodeDom.CodeAttributeDeclarationCollection that indicates the end of the attribute block to generate code for.
        """
        ...
    def GenerateAttributeDeclarationsStart(self, *args):  # cannot find CLR method
        """
        GenerateAttributeDeclarationsStart(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)

            Generates code for the specified attribute block start.

            attributes: A System.CodeDom.CodeAttributeDeclarationCollection that indicates the start of the attribute block to generate code for.
        """
        ...
    def GenerateBaseReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateBaseReferenceExpression(self: CodeGenerator, e: CodeBaseReferenceExpression)

            Generates code for the specified base reference expression.

            e: A System.CodeDom.CodeBaseReferenceExpression that indicates the expression to generate code for.
        """
        ...
    def GenerateBinaryOperatorExpression(self, *args):  # cannot find CLR method
        """
        GenerateBinaryOperatorExpression(self: CodeGenerator, e: CodeBinaryOperatorExpression)

            Generates code for the specified binary operator expression.

            e: A System.CodeDom.CodeBinaryOperatorExpression that indicates the expression to generate code for.
        """
        ...
    def GenerateCastExpression(self, *args):  # cannot find CLR method
        """
        GenerateCastExpression(self: CodeGenerator, e: CodeCastExpression)

            Generates code for the specified cast expression.

            e: A System.CodeDom.CodeCastExpression that indicates the expression to generate code for.
        """
        ...
    def GenerateCodeFromMember(self, member, writer, options):
        """
        GenerateCodeFromMember(self: CodeGenerator, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified class member using the specified text writer and code generator options.

            member: The class member to generate code for.

            writer: The text writer to output code to.

            options: The options to use when generating the code.
        """
        ...
    def GenerateComment(self, *args):  # cannot find CLR method
        """
        GenerateComment(self: CodeGenerator, e: CodeComment)

            Generates code for the specified comment.

            e: A System.CodeDom.CodeComment to generate code for.
        """
        ...
    def GenerateCommentStatement(self, *args):  # cannot find CLR method
        """
        GenerateCommentStatement(self: CodeGenerator, e: CodeCommentStatement)

            Generates code for the specified comment statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateCommentStatements(self, *args):  # cannot find CLR method
        """
        GenerateCommentStatements(self: CodeGenerator, e: CodeCommentStatementCollection)

            Generates code for the specified comment statements.

            e: The expression to generate code for.
        """
        ...
    def GenerateCompileUnit(self, *args):  # cannot find CLR method
        """
        GenerateCompileUnit(self: CodeGenerator, e: CodeCompileUnit)

            Generates code for the specified compile unit.

            e: The compile unit to generate code for.
        """
        ...
    def GenerateCompileUnitEnd(self, *args):  # cannot find CLR method
        """
        GenerateCompileUnitEnd(self: CodeGenerator, e: CodeCompileUnit)

            Generates code for the end of a compile unit.

            e: The compile unit to generate code for.
        """
        ...
    def GenerateCompileUnitStart(self, *args):  # cannot find CLR method
        """
        GenerateCompileUnitStart(self: CodeGenerator, e: CodeCompileUnit)

            Generates code for the start of a compile unit.

            e: The compile unit to generate code for.
        """
        ...
    def GenerateConditionStatement(self, *args):  # cannot find CLR method
        """
        GenerateConditionStatement(self: CodeGenerator, e: CodeConditionStatement)

            Generates code for the specified conditional statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateConstructor(self, *args):  # cannot find CLR method
        """
        GenerateConstructor(self: CodeGenerator, e: CodeConstructor, c: CodeTypeDeclaration)

            Generates code for the specified constructor.

            e: The constructor to generate code for.

            c: The type of the object that this constructor constructs.
        """
        ...
    def GenerateDecimalValue(self, *args):  # cannot find CLR method
        """
        GenerateDecimalValue(self: CodeGenerator, d: Decimal)

            Generates code for the specified decimal value.

            d: The decimal value to generate code for.
        """
        ...
    def GenerateDefaultValueExpression(self, *args):  # cannot find CLR method
        """
        GenerateDefaultValueExpression(self: CodeGenerator, e: CodeDefaultValueExpression)

            Generates code for the specified reference to a default value.

            e: The reference to generate code for.
        """
        ...
    def GenerateDelegateCreateExpression(self, *args):  # cannot find CLR method
        """
        GenerateDelegateCreateExpression(self: CodeGenerator, e: CodeDelegateCreateExpression)

            Generates code for the specified delegate creation expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateDelegateInvokeExpression(self, *args):  # cannot find CLR method
        """
        GenerateDelegateInvokeExpression(self: CodeGenerator, e: CodeDelegateInvokeExpression)

            Generates code for the specified delegate invoke expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateDirectionExpression(self, *args):  # cannot find CLR method
        """
        GenerateDirectionExpression(self: CodeGenerator, e: CodeDirectionExpression)

            Generates code for the specified direction expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateDirectives(self, *args):  # cannot find CLR method
        """
        GenerateDirectives(self: CodeGenerator, directives: CodeDirectiveCollection)

            Generates code for the specified code directives.

            directives: The code directives to generate code for.
        """
        ...
    def GenerateDoubleValue(self, *args):  # cannot find CLR method
        """
        GenerateDoubleValue(self: CodeGenerator, d: float)

            Generates code for a double-precision floating point number.

            d: The value to generate code for.
        """
        ...
    def GenerateEntryPointMethod(self, *args):  # cannot find CLR method
        """
        GenerateEntryPointMethod(self: CodeGenerator, e: CodeEntryPointMethod, c: CodeTypeDeclaration)

            Generates code for the specified entry point method.

            e: The entry point for the code.

            c: The code that declares the type.
        """
        ...
    def GenerateEvent(self, *args):  # cannot find CLR method
        """
        GenerateEvent(self: CodeGenerator, e: CodeMemberEvent, c: CodeTypeDeclaration)

            Generates code for the specified event.

            e: The member event to generate code for.

            c: The type of the object that this event occurs on.
        """
        ...
    def GenerateEventReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateEventReferenceExpression(self: CodeGenerator, e: CodeEventReferenceExpression)

            Generates code for the specified event reference expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateExpression(self, *args):  # cannot find CLR method
        """
        GenerateExpression(self: CodeGenerator, e: CodeExpression)

            Generates code for the specified code expression.

            e: The code expression to generate code for.
        """
        ...
    def GenerateExpressionStatement(self, *args):  # cannot find CLR method
        """
        GenerateExpressionStatement(self: CodeGenerator, e: CodeExpressionStatement)

            Generates code for the specified expression statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateField(self, *args):  # cannot find CLR method
        """
        GenerateField(self: CodeGenerator, e: CodeMemberField)

            Generates code for the specified member field.

            e: The field to generate code for.
        """
        ...
    def GenerateFieldReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateFieldReferenceExpression(self: CodeGenerator, e: CodeFieldReferenceExpression)

            Generates code for the specified field reference expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateGotoStatement(self, *args):  # cannot find CLR method
        """
        GenerateGotoStatement(self: CodeGenerator, e: CodeGotoStatement)

            Generates code for the specified to statement.

            e: The expression to generate code for.
        """
        ...
    def GenerateIndexerExpression(self, *args):  # cannot find CLR method
        """
        GenerateIndexerExpression(self: CodeGenerator, e: CodeIndexerExpression)

            Generates code for the specified indexer expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateIterationStatement(self, *args):  # cannot find CLR method
        """
        GenerateIterationStatement(self: CodeGenerator, e: CodeIterationStatement)

            Generates code for the specified iteration statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateLabeledStatement(self, *args):  # cannot find CLR method
        """
        GenerateLabeledStatement(self: CodeGenerator, e: CodeLabeledStatement)

            Generates code for the specified labeled statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateLinePragmaEnd(self, *args):  # cannot find CLR method
        """
        GenerateLinePragmaEnd(self: CodeGenerator, e: CodeLinePragma)

            Generates code for the specified line pragma end.

            e: The end of the line pragma to generate code for.
        """
        ...
    def GenerateLinePragmaStart(self, *args):  # cannot find CLR method
        """
        GenerateLinePragmaStart(self: CodeGenerator, e: CodeLinePragma)

            Generates code for the specified line pragma start.

            e: The start of the line pragma to generate code for.
        """
        ...
    def GenerateMethod(self, *args):  # cannot find CLR method
        """
        GenerateMethod(self: CodeGenerator, e: CodeMemberMethod, c: CodeTypeDeclaration)

            Generates code for the specified method.

            e: The member method to generate code for.

            c: The type of the object that this method occurs on.
        """
        ...
    def GenerateMethodInvokeExpression(self, *args):  # cannot find CLR method
        """
        GenerateMethodInvokeExpression(self: CodeGenerator, e: CodeMethodInvokeExpression)

            Generates code for the specified method invoke expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateMethodReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateMethodReferenceExpression(self: CodeGenerator, e: CodeMethodReferenceExpression)

            Generates code for the specified method reference expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateMethodReturnStatement(self, *args):  # cannot find CLR method
        """
        GenerateMethodReturnStatement(self: CodeGenerator, e: CodeMethodReturnStatement)

            Generates code for the specified method return statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateNamespace(self, *args):  # cannot find CLR method
        """
        GenerateNamespace(self: CodeGenerator, e: CodeNamespace)

            Generates code for the specified namespace.

            e: The namespace to generate code for.
        """
        ...
    def GenerateNamespaceEnd(self, *args):  # cannot find CLR method
        """
        GenerateNamespaceEnd(self: CodeGenerator, e: CodeNamespace)

            Generates code for the end of a namespace.

            e: The namespace to generate code for.
        """
        ...
    def GenerateNamespaceImport(self, *args):  # cannot find CLR method
        """
        GenerateNamespaceImport(self: CodeGenerator, e: CodeNamespaceImport)

            Generates code for the specified namespace import.

            e: The namespace import to generate code for.
        """
        ...
    def GenerateNamespaceImports(self, *args):  # cannot find CLR method
        """
        GenerateNamespaceImports(self: CodeGenerator, e: CodeNamespace)

            Generates code for the specified namespace import.

            e: The namespace import to generate code for.
        """
        ...
    def GenerateNamespaces(self, *args):  # cannot find CLR method
        """
        GenerateNamespaces(self: CodeGenerator, e: CodeCompileUnit)

            Generates code for the namespaces in the specified compile unit.

            e: The compile unit to generate namespaces for.
        """
        ...
    def GenerateNamespaceStart(self, *args):  # cannot find CLR method
        """
        GenerateNamespaceStart(self: CodeGenerator, e: CodeNamespace)

            Generates code for the start of a namespace.

            e: The namespace to generate code for.
        """
        ...
    def GenerateObjectCreateExpression(self, *args):  # cannot find CLR method
        """
        GenerateObjectCreateExpression(self: CodeGenerator, e: CodeObjectCreateExpression)

            Generates code for the specified object creation expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateParameterDeclarationExpression(self, *args):  # cannot find CLR method
        """
        GenerateParameterDeclarationExpression(self: CodeGenerator, e: CodeParameterDeclarationExpression)

            Generates code for the specified parameter declaration expression.

            e: The expression to generate code for.
        """
        ...
    def GeneratePrimitiveExpression(self, *args):  # cannot find CLR method
        """
        GeneratePrimitiveExpression(self: CodeGenerator, e: CodePrimitiveExpression)

            Generates code for the specified primitive expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateProperty(self, *args):  # cannot find CLR method
        """
        GenerateProperty(self: CodeGenerator, e: CodeMemberProperty, c: CodeTypeDeclaration)

            Generates code for the specified property.

            e: The property to generate code for.

            c: The type of the object that this property occurs on.
        """
        ...
    def GeneratePropertyReferenceExpression(self, *args):  # cannot find CLR method
        """
        GeneratePropertyReferenceExpression(self: CodeGenerator, e: CodePropertyReferenceExpression)

            Generates code for the specified property reference expression.

            e: The expression to generate code for.
        """
        ...
    def GeneratePropertySetValueReferenceExpression(self, *args):  # cannot find CLR method
        """
        GeneratePropertySetValueReferenceExpression(self: CodeGenerator, e: CodePropertySetValueReferenceExpression)

            Generates code for the specified property set value reference expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateRemoveEventStatement(self, *args):  # cannot find CLR method
        """
        GenerateRemoveEventStatement(self: CodeGenerator, e: CodeRemoveEventStatement)

            Generates code for the specified remove event statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateSingleFloatValue(self, *args):  # cannot find CLR method
        """
        GenerateSingleFloatValue(self: CodeGenerator, s: Single)

            Generates code for a single-precision floating point number.

            s: The value to generate code for.
        """
        ...
    def GenerateSnippetCompileUnit(self, *args):  # cannot find CLR method
        """
        GenerateSnippetCompileUnit(self: CodeGenerator, e: CodeSnippetCompileUnit)

            Outputs the code of the specified literal code fragment compile unit.

            e: The literal code fragment compile unit to generate code for.
        """
        ...
    def GenerateSnippetExpression(self, *args):  # cannot find CLR method
        """
        GenerateSnippetExpression(self: CodeGenerator, e: CodeSnippetExpression)

            Outputs the code of the specified literal code fragment expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateSnippetMember(self, *args):  # cannot find CLR method
        """
        GenerateSnippetMember(self: CodeGenerator, e: CodeSnippetTypeMember)

            Outputs the code of the specified literal code fragment class member.

            e: The member to generate code for.
        """
        ...
    def GenerateSnippetStatement(self, *args):  # cannot find CLR method
        """
        GenerateSnippetStatement(self: CodeGenerator, e: CodeSnippetStatement)

            Outputs the code of the specified literal code fragment statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateStatement(self, *args):  # cannot find CLR method
        """
        GenerateStatement(self: CodeGenerator, e: CodeStatement)

            Generates code for the specified statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateStatements(self, *args):  # cannot find CLR method
        """
        GenerateStatements(self: CodeGenerator, stms: CodeStatementCollection)

            Generates code for the specified statement collection.

            stms: The statements to generate code for.
        """
        ...
    def GenerateThisReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateThisReferenceExpression(self: CodeGenerator, e: CodeThisReferenceExpression)

            Generates code for the specified this reference expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateThrowExceptionStatement(self, *args):  # cannot find CLR method
        """
        GenerateThrowExceptionStatement(self: CodeGenerator, e: CodeThrowExceptionStatement)

            Generates code for the specified throw exception statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateTryCatchFinallyStatement(self, *args):  # cannot find CLR method
        """
        GenerateTryCatchFinallyStatement(self: CodeGenerator, e: CodeTryCatchFinallyStatement)

            Generates code for the specified y...catch...finally statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateTypeConstructor(self, *args):  # cannot find CLR method
        """
        GenerateTypeConstructor(self: CodeGenerator, e: CodeTypeConstructor)

            Generates code for the specified class constructor.

            e: The class constructor to generate code for.
        """
        ...
    def GenerateTypeEnd(self, *args):  # cannot find CLR method
        """
        GenerateTypeEnd(self: CodeGenerator, e: CodeTypeDeclaration)

            Generates code for the specified end of the class.

            e: The end of the class to generate code for.
        """
        ...
    def GenerateTypeOfExpression(self, *args):  # cannot find CLR method
        """
        GenerateTypeOfExpression(self: CodeGenerator, e: CodeTypeOfExpression)

            Generates code for the specified type of expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateTypeReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateTypeReferenceExpression(self: CodeGenerator, e: CodeTypeReferenceExpression)

            Generates code for the specified type reference expression.

            e: The expression to generate code for.
        """
        ...
    def GenerateTypes(self, *args):  # cannot find CLR method
        """
        GenerateTypes(self: CodeGenerator, e: CodeNamespace)

            Generates code for the specified namespace and the classes it contains.

            e: The namespace to generate classes for.
        """
        ...
    def GenerateTypeStart(self, *args):  # cannot find CLR method
        """
        GenerateTypeStart(self: CodeGenerator, e: CodeTypeDeclaration)

            Generates code for the specified start of the class.

            e: The start of the class to generate code for.
        """
        ...
    def GenerateVariableDeclarationStatement(self, *args):  # cannot find CLR method
        """
        GenerateVariableDeclarationStatement(self: CodeGenerator, e: CodeVariableDeclarationStatement)

            Generates code for the specified variable declaration statement.

            e: The statement to generate code for.
        """
        ...
    def GenerateVariableReferenceExpression(self, *args):  # cannot find CLR method
        """
        GenerateVariableReferenceExpression(self: CodeGenerator, e: CodeVariableReferenceExpression)

            Generates code for the specified variable reference expression.

            e: The expression to generate code for.
        """
        ...
    @staticmethod
    def IsValidLanguageIndependentIdentifier(value):
        """
        IsValidLanguageIndependentIdentifier(value: str) -> bool

            Gets a value indicating whether the specified string is a valid identifier.

            value: The string to test for validity.

            Returns: ue if the specified string is a valid identifier; otherwise, lse.
        """
        ...
    def OutputAttributeArgument(self, *args):  # cannot find CLR method
        """
        OutputAttributeArgument(self: CodeGenerator, arg: CodeAttributeArgument)

            Outputs an argument in an attribute block.

            arg: The attribute argument to generate code for.
        """
        ...
    def OutputAttributeDeclarations(self, *args):  # cannot find CLR method
        """
        OutputAttributeDeclarations(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)

            Generates code for the specified attribute declaration collection.

            attributes: The attributes to generate code for.
        """
        ...
    def OutputDirection(self, *args):  # cannot find CLR method
        """
        OutputDirection(self: CodeGenerator, dir: FieldDirection)

            Generates code for the specified System.CodeDom.FieldDirection.

            dir: One of the enumeration values that indicates the attribute of the field.
        """
        ...
    def OutputExpressionList(self, *args):  # cannot find CLR method
        """
        OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection)

            Generates code for the specified expression list.

            expressions: The expressions to generate code for.

        OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection, newlineBetweenItems: bool)

            Generates code for the specified expression list.

            expressions: The expressions to generate code for.

            newlineBetweenItems: ue to insert a new line after each item; otherwise, lse.
        """
        ...
    def OutputFieldScopeModifier(self, *args):  # cannot find CLR method
        """
        OutputFieldScopeModifier(self: CodeGenerator, attributes: MemberAttributes)

            Outputs a field scope modifier that corresponds to the specified attributes.

            attributes: One of the enumeration values that specifies the attributes.
        """
        ...
    def OutputIdentifier(self, *args):  # cannot find CLR method
        """
        OutputIdentifier(self: CodeGenerator, ident: str)

            Outputs the specified identifier.

            ident: The identifier to output.
        """
        ...
    def OutputMemberAccessModifier(self, *args):  # cannot find CLR method
        """
        OutputMemberAccessModifier(self: CodeGenerator, attributes: MemberAttributes)

            Generates code for the specified member access modifier.

            attributes: One of the enumeration values that indicates the member access modifier to generate code for.
        """
        ...
    def OutputMemberScopeModifier(self, *args):  # cannot find CLR method
        """
        OutputMemberScopeModifier(self: CodeGenerator, attributes: MemberAttributes)

            Generates code for the specified member scope modifier.

            attributes: One of the enumeration values that indicates the member scope modifier to generate code for.
        """
        ...
    def OutputOperator(self, *args):  # cannot find CLR method
        """
        OutputOperator(self: CodeGenerator, op: CodeBinaryOperatorType)

            Generates code for the specified operator.

            op: The operator to generate code for.
        """
        ...
    def OutputParameters(self, *args):  # cannot find CLR method
        """
        OutputParameters(self: CodeGenerator, parameters: CodeParameterDeclarationExpressionCollection)

            Generates code for the specified parameters.

            parameters: The parameter declaration expressions to generate code for.
        """
        ...
    def OutputType(self, *args):  # cannot find CLR method
        """
        OutputType(self: CodeGenerator, typeRef: CodeTypeReference)

            Generates code for the specified type.

            typeRef: The type to generate code for.
        """
        ...
    def OutputTypeAttributes(self, *args):  # cannot find CLR method
        """
        OutputTypeAttributes(self: CodeGenerator, attributes: TypeAttributes, isStruct: bool, isEnum: bool)

            Generates code for the specified type attributes.

            attributes: One of the enumeration values that indicates the type attributes to generate code for.

            isStruct: ue if the type is a struct; otherwise, lse.

            isEnum: ue if the type is an enum; otherwise, lse.
        """
        ...
    def OutputTypeNamePair(self, *args):  # cannot find CLR method
        """
        OutputTypeNamePair(self: CodeGenerator, typeRef: CodeTypeReference, name: str)

            Generates code for the specified object type and name pair.

            typeRef: The type.

            name: The name for the object.
        """
        ...
    def QuoteSnippetString(self, *args):  # cannot find CLR method
        """
        QuoteSnippetString(self: CodeGenerator, value: str) -> str

            Converts the specified string by formatting it with escape codes.

            value: The string to convert.

            Returns: The converted string.
        """
        ...
    @staticmethod
    def ValidateIdentifiers(e):
        """
        ValidateIdentifiers(e: CodeObject)

            Attempts to validate each identifier field contained in the specified System.CodeDom.CodeObject or System.CodeDom tree.

            e: An object to test for invalid identifiers.
        """
        ...
    @property
    def CurrentClass(self):
        """Gets the code type declaration for the current class."""
        ...
    @property
    def CurrentMember(self):
        """Gets the current member of the class."""
        ...
    @property
    def CurrentMemberName(self):
        """Gets the current member name."""
        ...
    @property
    def CurrentTypeName(self):
        """Gets the current class name."""
        ...
    @property
    def Indent(self):
        """Gets or sets the amount of spaces to indent each indentation level."""
        ...
    @property
    def IsCurrentClass(self):
        """Gets a value indicating whether the current object being generated is a class."""
        ...
    @property
    def IsCurrentDelegate(self):
        """Gets a value indicating whether the current object being generated is a delegate."""
        ...
    @property
    def IsCurrentEnum(self):
        """Gets a value indicating whether the current object being generated is an enumeration."""
        ...
    @property
    def IsCurrentInterface(self):
        """Gets a value indicating whether the current object being generated is an interface."""
        ...
    @property
    def IsCurrentStruct(self):
        """Gets a value indicating whether the current object being generated is a value type or struct."""
        ...
    @property
    def NullToken(self):
        """Gets the token that represents ll."""
        ...
    @property
    def Options(self):
        """Gets the options to be used by the code generator."""
        ...
    @property
    def Output(self):
        """Gets the text writer to use for output."""
        ...

class ICodeCompiler:
    """Defines an interface for invoking compilation of source code or a CodeDOM tree using a specific compiler."""

    def CompileAssemblyFromDom(self, options, compilationUnit):
        """
        CompileAssemblyFromDom(self: ICodeCompiler, options: CompilerParameters, compilationUnit: CodeCompileUnit) -> CompilerResults

            Compiles an assembly from the System.CodeDom tree contained in the specified System.CodeDom.CodeCompileUnit, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.

            compilationUnit: A System.CodeDom.CodeCompileUnit that indicates the code to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CompileAssemblyFromDomBatch(self, options, compilationUnits):
        """
        CompileAssemblyFromDomBatch(self: ICodeCompiler, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]) -> CompilerResults

            Compiles an assembly based on the System.CodeDom trees contained in the specified array of System.CodeDom.CodeCompileUnit objects, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.

            compilationUnits: An array of type System.CodeDom.CodeCompileUnit that indicates the code to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CompileAssemblyFromFile(self, options, fileName):
        """
        CompileAssemblyFromFile(self: ICodeCompiler, options: CompilerParameters, fileName: str) -> CompilerResults

            Compiles an assembly from the source code contained within the specified file, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.

            fileName: The file name of the file that contains the source code to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CompileAssemblyFromFileBatch(self, options, fileNames):
        """
        CompileAssemblyFromFileBatch(self: ICodeCompiler, options: CompilerParameters, fileNames: Array[str]) -> CompilerResults

            Compiles an assembly from the source code contained within the specified files, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.

            fileNames: The file names of the files to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CompileAssemblyFromSource(self, options, source):
        """
        CompileAssemblyFromSource(self: ICodeCompiler, options: CompilerParameters, source: str) -> CompilerResults

            Compiles an assembly from the specified string containing source code, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.

            source: The source code to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CompileAssemblyFromSourceBatch(self, options, sources):
        """
        CompileAssemblyFromSourceBatch(self: ICodeCompiler, options: CompilerParameters, sources: Array[str]) -> CompilerResults

            Compiles an assembly from the specified array of strings containing source code, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.

            sources: The source code strings to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...

class CodeCompiler(CodeGenerator, ICodeCompiler):  # skipped bases: <type 'ICodeGenerator'>
    """Provides an example implementation of the System.CodeDom.Compiler.ICodeCompiler interface."""

    def CmdArgsFromParameters(self, *args):  # cannot find CLR method
        """
        CmdArgsFromParameters(self: CodeCompiler, options: CompilerParameters) -> str

            Gets the command arguments to be passed to the compiler from the specified System.CodeDom.Compiler.CompilerParameters.

            options: A System.CodeDom.Compiler.CompilerParameters that indicates the compiler options.

            Returns: The command arguments.
        """
        ...
    def FromDom(self, *args):  # cannot find CLR method
        """
        FromDom(self: CodeCompiler, options: CompilerParameters, e: CodeCompileUnit) -> CompilerResults

            Compiles the specified compile unit using the specified options, and returns the results from the compilation.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            e: A System.CodeDom.CodeCompileUnit object that indicates the source to compile.

            Returns: The results of compilation.
        """
        ...
    def FromDomBatch(self, *args):  # cannot find CLR method
        """
        FromDomBatch(self: CodeCompiler, options: CompilerParameters, ea: Array[CodeCompileUnit]) -> CompilerResults

            Compiles the specified compile units using the specified options, and returns the results from the compilation.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            ea: An array of System.CodeDom.CodeCompileUnit objects that indicates the source to compile.

            Returns: The results of compilation.
        """
        ...
    def FromFile(self, *args):  # cannot find CLR method
        """
        FromFile(self: CodeCompiler, options: CompilerParameters, fileName: str) -> CompilerResults

            Compiles the specified file using the specified options, and returns the results from the compilation.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            fileName: The file name to compile.

            Returns: The results of compilation.
        """
        ...
    def FromFileBatch(self, *args):  # cannot find CLR method
        """
        FromFileBatch(self: CodeCompiler, options: CompilerParameters, fileNames: Array[str]) -> CompilerResults

            Compiles the specified files using the specified options, and returns the results from the compilation.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            fileNames: An array of strings that indicates the file names of the files to compile.

            Returns: The results of compilation.
        """
        ...
    def FromSource(self, *args):  # cannot find CLR method
        """
        FromSource(self: CodeCompiler, options: CompilerParameters, source: str) -> CompilerResults

            Compiles the specified source code string using the specified options, and returns the results from the compilation.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            source: The source code string to compile.

            Returns: The results of compilation.
        """
        ...
    def FromSourceBatch(self, *args):  # cannot find CLR method
        """
        FromSourceBatch(self: CodeCompiler, options: CompilerParameters, sources: Array[str]) -> CompilerResults

            Compiles the specified source code strings using the specified options, and returns the results from the compilation.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            sources: An array of strings containing the source code to compile.

            Returns: The results of compilation.
        """
        ...
    def GetResponseFileCmdArgs(self, *args):  # cannot find CLR method
        """
        GetResponseFileCmdArgs(self: CodeCompiler, options: CompilerParameters, cmdArgs: str) -> str

            Gets the command arguments to use when invoking the compiler to generate a response file.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.

            cmdArgs: A command arguments string.

            Returns: The command arguments to use to generate a response file, or ll if there are no response file arguments.
        """
        ...
    def JoinStringArray(self, *args):  # cannot find CLR method
        """
        JoinStringArray(sa: Array[str], separator: str) -> str

            Joins the specified string arrays.

            sa: The array of strings to join.

            separator: The separator to use.

            Returns: The concatenated string.
        """
        ...
    def ProcessCompilerOutputLine(self, *args):  # cannot find CLR method
        """
        ProcessCompilerOutputLine(self: CodeCompiler, results: CompilerResults, line: str)

            Processes the specified line from the specified System.CodeDom.Compiler.CompilerResults.

            results: A System.CodeDom.Compiler.CompilerResults that indicates the results of compilation.

            line: The line to process.
        """
        ...
    @property
    def CompilerName(self):
        """Gets the name of the compiler executable."""
        ...
    @property
    def CurrentClass(self):
        """Gets the code type declaration for the current class."""
        ...
    @property
    def CurrentMember(self):
        """Gets the current member of the class."""
        ...
    @property
    def CurrentMemberName(self):
        """Gets the current member name."""
        ...
    @property
    def CurrentTypeName(self):
        """Gets the current class name."""
        ...
    @property
    def FileExtension(self):
        """Gets the file name extension to use for source files."""
        ...
    @property
    def Indent(self):
        """Gets or sets the amount of spaces to indent each indentation level."""
        ...
    @property
    def IsCurrentClass(self):
        """Gets a value indicating whether the current object being generated is a class."""
        ...
    @property
    def IsCurrentDelegate(self):
        """Gets a value indicating whether the current object being generated is a delegate."""
        ...
    @property
    def IsCurrentEnum(self):
        """Gets a value indicating whether the current object being generated is an enumeration."""
        ...
    @property
    def IsCurrentInterface(self):
        """Gets a value indicating whether the current object being generated is an interface."""
        ...
    @property
    def IsCurrentStruct(self):
        """Gets a value indicating whether the current object being generated is a value type or struct."""
        ...
    @property
    def NullToken(self):
        """Gets the token that represents ll."""
        ...
    @property
    def Options(self):
        """Gets the options to be used by the code generator."""
        ...
    @property
    def Output(self):
        """Gets the text writer to use for output."""
        ...

class CodeDomProvider(Component):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """Provides a base class for System.CodeDom.Compiler.CodeDomProvider implementations. This class is abstract."""

    def CompileAssemblyFromDom(self, options, compilationUnits):
        """
        CompileAssemblyFromDom(self: CodeDomProvider, options: CompilerParameters, *compilationUnits: Array[CodeCompileUnit]) -> CompilerResults

            Compiles an assembly based on the System.CodeDom trees contained in the specified array of System.CodeDom.CodeCompileUnit objects, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for the compilation.

            compilationUnits: An array of type System.CodeDom.CodeCompileUnit that indicates the code to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of the compilation.
        """
        ...
    def CompileAssemblyFromFile(self, options, fileNames):
        """
        CompileAssemblyFromFile(self: CodeDomProvider, options: CompilerParameters, *fileNames: Array[str]) -> CompilerResults

            Compiles an assembly from the source code contained in the specified files, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for the compilation.

            fileNames: An array of the names of the files to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CompileAssemblyFromSource(self, options, sources):
        """
        CompileAssemblyFromSource(self: CodeDomProvider, options: CompilerParameters, *sources: Array[str]) -> CompilerResults

            Compiles an assembly from the specified array of strings containing source code, using the specified compiler settings.

            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler settings for this compilation.

            sources: An array of source code strings to compile.

            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        ...
    def CreateCompiler(self):
        """
        CreateCompiler(self: CodeDomProvider) -> ICodeCompiler

            When overridden in a derived class, creates a new code compiler.

            Returns: An System.CodeDom.Compiler.ICodeCompiler that can be used for compilation of System.CodeDom based source code representations.
        """
        ...
    def CreateEscapedIdentifier(self, value):
        """
        CreateEscapedIdentifier(self: CodeDomProvider, value: str) -> str

            Creates an escaped identifier for the specified value.

            value: The string for which to create an escaped identifier.

            Returns: The escaped identifier for the value.
        """
        ...
    def CreateGenerator(self, *__args):
        """
        CreateGenerator(self: CodeDomProvider, output: TextWriter) -> ICodeGenerator

            When overridden in a derived class, creates a new code generator using the specified System.IO.TextWriter for output.

            output: A System.IO.TextWriter to use to output.

            Returns: An System.CodeDom.Compiler.ICodeGenerator that can be used to generate System.CodeDom based source code representations.

        CreateGenerator(self: CodeDomProvider, fileName: str) -> ICodeGenerator

            When overridden in a derived class, creates a new code generator using the specified file name for output.

            fileName: The file name to output to.

            Returns: An System.CodeDom.Compiler.ICodeGenerator that can be used to generate System.CodeDom based source code representations.

        CreateGenerator(self: CodeDomProvider) -> ICodeGenerator

            When overridden in a derived class, creates a new code generator.

            Returns: An System.CodeDom.Compiler.ICodeGenerator that can be used to generate System.CodeDom based source code representations.
        """
        ...
    def CreateParser(self):
        """
        CreateParser(self: CodeDomProvider) -> ICodeParser

            When overridden in a derived class, creates a new code parser.

            Returns: An System.CodeDom.Compiler.ICodeParser that can be used to parse source code. The base implementation always returns ll.
        """
        ...
    @staticmethod
    def CreateProvider(language, providerOptions=None):
        """
        CreateProvider(language: str, providerOptions: IDictionary[str, str]) -> CodeDomProvider

        CreateProvider(language: str) -> CodeDomProvider

            Gets a System.CodeDom.Compiler.CodeDomProvider instance for the specified language.

            language: The language name.

            Returns: A CodeDOM provider that is implemented for the specified language name.
        """
        ...
    def CreateValidIdentifier(self, value):
        """
        CreateValidIdentifier(self: CodeDomProvider, value: str) -> str

            Creates a valid identifier for the specified value.

            value: The string for which to generate a valid identifier.

            Returns: A valid identifier for the specified value.
        """
        ...
    def GenerateCodeFromCompileUnit(self, compileUnit, writer, options):
        """
        GenerateCodeFromCompileUnit(self: CodeDomProvider, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) compilation unit and sends it to the specified text writer, using the specified options.

            compileUnit: A System.CodeDom.CodeCompileUnit for which to generate code.

            writer: The System.IO.TextWriter to which the output code is sent.

            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromExpression(self, expression, writer, options):
        """
        GenerateCodeFromExpression(self: CodeDomProvider, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) expression and sends it to the specified text writer, using the specified options.

            expression: A System.CodeDom.CodeExpression object that indicates the expression for which to generate code.

            writer: The System.IO.TextWriter to which output code is sent.

            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromMember(self, member, writer, options):
        """
        GenerateCodeFromMember(self: CodeDomProvider, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) member declaration and sends it to the specified text writer, using the specified options.

            member: A System.CodeDom.CodeTypeMember object that indicates the member for which to generate code.

            writer: The System.IO.TextWriter to which output code is sent.

            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromNamespace(self, codeNamespace, writer, options):
        """
        GenerateCodeFromNamespace(self: CodeDomProvider, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) namespace and sends it to the specified text writer, using the specified options.

            codeNamespace: A System.CodeDom.CodeNamespace object that indicates the namespace for which to generate code.

            writer: The System.IO.TextWriter to which output code is sent.

            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromStatement(self, statement, writer, options):
        """
        GenerateCodeFromStatement(self: CodeDomProvider, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) statement and sends it to the specified text writer, using the specified options.

            statement: A System.CodeDom.CodeStatement containing the CodeDOM elements for which to generate code.

            writer: The System.IO.TextWriter to which output code is sent.

            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    def GenerateCodeFromType(self, codeType, writer, options):
        """
        GenerateCodeFromType(self: CodeDomProvider, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions)

            Generates code for the specified Code Document Object Model (CodeDOM) type declaration and sends it to the specified text writer, using the specified options.

            codeType: A System.CodeDom.CodeTypeDeclaration object that indicates the type for which to generate code.

            writer: The System.IO.TextWriter to which output code is sent.

            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating code.
        """
        ...
    @staticmethod
    def GetAllCompilerInfo():
        """
        GetAllCompilerInfo() -> Array[CompilerInfo]

            Returns the language provider and compiler configuration settings for this computer.

            Returns: An array of type System.CodeDom.Compiler.CompilerInfo representing the settings of all configured System.CodeDom.Compiler.CodeDomProvider implementations.
        """
        ...
    @staticmethod
    def GetCompilerInfo(language):
        """
        GetCompilerInfo(language: str) -> CompilerInfo

            Returns the language provider and compiler configuration settings for the specified language.

            language: A language name.

            Returns: A System.CodeDom.Compiler.CompilerInfo object populated with settings of the configured System.CodeDom.Compiler.CodeDomProvider implementation.
        """
        ...
    def GetConverter(self, type):
        """
        GetConverter(self: CodeDomProvider, type: Type) -> TypeConverter

            Gets a System.ComponentModel.TypeConverter for the specified data type.

            type: The type of object to retrieve a type converter for.

            Returns: A System.ComponentModel.TypeConverter for the specified type, or ll if a System.ComponentModel.TypeConverter for the specified type cannot be found.
        """
        ...
    @staticmethod
    def GetLanguageFromExtension(extension):
        """
        GetLanguageFromExtension(extension: str) -> str

            Returns a language name associated with the specified file name extension, as configured in the System.CodeDom.Compiler.CodeDomProvider compiler configuration section.

            extension: A file name extension.

            Returns: A language name associated with the file name extension, as configured in the System.CodeDom.Compiler.CodeDomProvider compiler configuration settings.
        """
        ...
    def GetTypeOutput(self, type):
        """
        GetTypeOutput(self: CodeDomProvider, type: CodeTypeReference) -> str

            Gets the type indicated by the specified System.CodeDom.CodeTypeReference.

            type: A System.CodeDom.CodeTypeReference that indicates the type to return.

            Returns: A text representation of the specified type, formatted for the language in which code is generated by this code generator. In Visual Basic, for example, passing in a System.CodeDom.CodeTypeReference for the System.Int32 type will

             return "Integer".
        """
        ...
    @staticmethod
    def IsDefinedExtension(extension):
        """
        IsDefinedExtension(extension: str) -> bool

            Tests whether a file name extension has an associated System.CodeDom.Compiler.CodeDomProvider implementation configured on the computer.

            extension: A file name extension.

            Returns: ue if a System.CodeDom.Compiler.CodeDomProvider implementation is configured for the specified file name extension; otherwise, lse.
        """
        ...
    @staticmethod
    def IsDefinedLanguage(language):
        """
        IsDefinedLanguage(language: str) -> bool

            Tests whether a language has a System.CodeDom.Compiler.CodeDomProvider implementation configured on the computer.

            language: The language name.

            Returns: ue if a System.CodeDom.Compiler.CodeDomProvider implementation is configured for the specified language; otherwise, lse.
        """
        ...
    def IsValidIdentifier(self, value):
        """
        IsValidIdentifier(self: CodeDomProvider, value: str) -> bool

            Returns a value that indicates whether the specified value is a valid identifier for the current language.

            value: The value to verify as a valid identifier.

            Returns: ue if the value parameter is a valid identifier; otherwise, lse.
        """
        ...
    def Parse(self, codeStream):
        """
        Parse(self: CodeDomProvider, codeStream: TextReader) -> CodeCompileUnit

            Compiles the code read from the specified text stream into a System.CodeDom.CodeCompileUnit.

            codeStream: A System.IO.TextReader object that is used to read the code to be parsed.

            Returns: A System.CodeDom.CodeCompileUnit that contains a representation of the parsed code.
        """
        ...
    def Supports(self, generatorSupport):
        """
        Supports(self: CodeDomProvider, generatorSupport: GeneratorSupport) -> bool

            Returns a value indicating whether the specified code generation support is provided.

            generatorSupport: A System.CodeDom.Compiler.GeneratorSupport object that indicates the type of code generation support to verify.

            Returns: ue if the specified code generation support is provided; otherwise, lse.
        """
        ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def FileExtension(self):
        """
        Gets the default file name extension to use for source code files in the current language.

        Get: FileExtension(self: CodeDomProvider) -> str
        """
        ...
    @property
    def LanguageOptions(self):
        """
        Gets a language features identifier.

        Get: LanguageOptions(self: CodeDomProvider) -> LanguageOptions
        """
        ...

class CodeGeneratorOptions:  # skipped bases: <type 'object'>
    """
    Represents a set of options used by a code generator.

    CodeGeneratorOptions()
    """

    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def BlankLinesBetweenMembers(self):
        """
        Gets or sets a value indicating whether to insert blank lines between members.

        Get: BlankLinesBetweenMembers(self: CodeGeneratorOptions) -> bool

        Set: BlankLinesBetweenMembers(self: CodeGeneratorOptions) = value
        """
        ...
    @property
    def BracingStyle(self):
        """
        Gets or sets the style to use for bracing.

        Get: BracingStyle(self: CodeGeneratorOptions) -> str

        Set: BracingStyle(self: CodeGeneratorOptions) = value
        """
        ...
    @property
    def ElseOnClosing(self):
        """
        Gets or sets a value indicating whether to append an se, tch, or nally block, including brackets, at the closing line of each previous  or y block.

        Get: ElseOnClosing(self: CodeGeneratorOptions) -> bool

        Set: ElseOnClosing(self: CodeGeneratorOptions) = value
        """
        ...
    @property
    def IndentString(self):
        """
        Gets or sets the string to use for indentations.

        Get: IndentString(self: CodeGeneratorOptions) -> str

        Set: IndentString(self: CodeGeneratorOptions) = value
        """
        ...
    @property
    def VerbatimOrder(self):
        """
        Gets or sets a value indicating whether to generate members in the order in which they occur in member collections.

        Get: VerbatimOrder(self: CodeGeneratorOptions) -> bool

        Set: VerbatimOrder(self: CodeGeneratorOptions) = value
        """
        ...

class CodeParser(ICodeParser):
    """Provides an empty implementation of the System.CodeDom.Compiler.ICodeParser interface."""

    pass

class CompilerError:  # skipped bases: <type 'object'>
    """
    Represents a compiler error or warning.

    CompilerError()

    CompilerError(fileName: str, line: int, column: int, errorNumber: str, errorText: str)
    """

    def ToString(self):
        """
        ToString(self: CompilerError) -> str

            Provides an implementation of Object's System.Object.ToString method.

            Returns: A string representation of the compiler error.
        """
        ...
    @property
    def Column(self):
        """
        Gets or sets the column number where the source of the error occurs.

        Get: Column(self: CompilerError) -> int

        Set: Column(self: CompilerError) = value
        """
        ...
    @property
    def ErrorNumber(self):
        """
        Gets or sets the error number.

        Get: ErrorNumber(self: CompilerError) -> str

        Set: ErrorNumber(self: CompilerError) = value
        """
        ...
    @property
    def ErrorText(self):
        """
        Gets or sets the text of the error message.

        Get: ErrorText(self: CompilerError) -> str

        Set: ErrorText(self: CompilerError) = value
        """
        ...
    @property
    def FileName(self):
        """
        Gets or sets the file name of the source file that contains the code which caused the error.

        Get: FileName(self: CompilerError) -> str

        Set: FileName(self: CompilerError) = value
        """
        ...
    @property
    def IsWarning(self):
        """
        Gets or sets a value that indicates whether the error is a warning.

        Get: IsWarning(self: CompilerError) -> bool

        Set: IsWarning(self: CompilerError) = value
        """
        ...
    @property
    def Line(self):
        """
        Gets or sets the line number where the source of the error occurs.

        Get: Line(self: CompilerError) -> int

        Set: Line(self: CompilerError) = value
        """
        ...

class CompilerErrorCollection(
    CollectionBase
):  # skipped bases: <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>
    """
    Represents a collection of System.CodeDom.Compiler.CompilerError objects.

    CompilerErrorCollection()

    CompilerErrorCollection(value: CompilerErrorCollection)

    CompilerErrorCollection(value: Array[CompilerError])
    """

    def Add(self, value):
        """
        Add(self: CompilerErrorCollection, value: CompilerError) -> int

            Adds the specified System.CodeDom.Compiler.CompilerError object to the error collection.

            value: The System.CodeDom.Compiler.CompilerError object to add.

            Returns: The index at which the new element was inserted.
        """
        ...
    def AddRange(self, value):
        """
        AddRange(self: CompilerErrorCollection, value: Array[CompilerError])

            Copies the elements of an array to the end of the error collection.

            value: An array of type System.CodeDom.Compiler.CompilerError that contains the objects to add to the collection.

        AddRange(self: CompilerErrorCollection, value: CompilerErrorCollection)

            Adds the contents of the specified compiler error collection to the end of the error collection.

            value: A System.CodeDom.Compiler.CompilerErrorCollection object that contains the objects to add to the collection.
        """
        ...
    def Contains(self, value):
        """
        Contains(self: CompilerErrorCollection, value: CompilerError) -> bool

            Gets a value that indicates whether the collection contains the specified System.CodeDom.Compiler.CompilerError object.

            value: The System.CodeDom.Compiler.CompilerError to locate.

            Returns: ue if the System.CodeDom.Compiler.CompilerError is contained in the collection; otherwise, lse.
        """
        ...
    def CopyTo(self, array, index):
        """
        CopyTo(self: CompilerErrorCollection, array: Array[CompilerError], index: int)

            Copies the collection values to a one-dimensional System.Array instance at the specified index.

            array: The one-dimensional System.Array that is the destination of the values copied from System.CodeDom.Compiler.CompilerErrorCollection.

            index: The index in the array at which to start copying.
        """
        ...
    def IndexOf(self, value):
        """
        IndexOf(self: CompilerErrorCollection, value: CompilerError) -> int

            Gets the index of the specified System.CodeDom.Compiler.CompilerError object in the collection, if it exists in the collection.

            value: The System.CodeDom.Compiler.CompilerError to locate.

            Returns: The index of the specified System.CodeDom.Compiler.CompilerError in the System.CodeDom.Compiler.CompilerErrorCollection, if found; otherwise, -1.
        """
        ...
    def Insert(self, index, value):
        """
        Insert(self: CompilerErrorCollection, index: int, value: CompilerError)

            Inserts the specified System.CodeDom.Compiler.CompilerError into the collection at the specified index.

            index: The zero-based index where the compiler error should be inserted.

            value: The System.CodeDom.Compiler.CompilerError to insert.
        """
        ...
    def Remove(self, value):
        """
        Remove(self: CompilerErrorCollection, value: CompilerError)

            Removes a specific System.CodeDom.Compiler.CompilerError from the collection.

            value: The System.CodeDom.Compiler.CompilerError to remove from the System.CodeDom.Compiler.CompilerErrorCollection.
        """
        ...
    def __add__(self, *args):  # cannot find CLR method
        """x.__add__(y) <==> x+y"""
        ...
    def __getitem__(self, *args):  # cannot find CLR method
        """x.__getitem__(y) <==> x[y]"""
        ...
    def __setitem__(self, *args):  # cannot find CLR method
        """x.__setitem__(i, y) <==> x[i]="""
        ...
    @property
    def HasErrors(self):
        """
        Gets a value that indicates whether the collection contains errors.

        Get: HasErrors(self: CompilerErrorCollection) -> bool
        """
        ...
    @property
    def HasWarnings(self):
        """
        Gets a value that indicates whether the collection contains warnings.

        Get: HasWarnings(self: CompilerErrorCollection) -> bool
        """
        ...
    @property
    def InnerList(self):
        """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...
    @property
    def List(self):
        """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance."""
        ...

class CompilerInfo:  # skipped bases: <type 'object'>
    """Represents the configuration settings of a language provider. This class cannot be inherited."""

    def CreateDefaultCompilerParameters(self):
        """
        CreateDefaultCompilerParameters(self: CompilerInfo) -> CompilerParameters

            Gets the configured compiler settings for the language provider implementation.

            Returns: A read-only System.CodeDom.Compiler.CompilerParameters instance that contains the compiler options and settings configured for the language provider.
        """
        ...
    def CreateProvider(self, providerOptions=None):
        """
        CreateProvider(self: CompilerInfo) -> CodeDomProvider

            Returns a System.CodeDom.Compiler.CodeDomProvider instance for the current language provider settings.

            Returns: A CodeDOM provider associated with the language provider configuration.

        CreateProvider(self: CompilerInfo, providerOptions: IDictionary[str, str]) -> CodeDomProvider
        """
        ...
    def Equals(self, o):
        """
        Equals(self: CompilerInfo, o: object) -> bool

            Determines whether the specified object represents the same language provider and compiler settings as the current System.CodeDom.Compiler.CompilerInfo.

            o: The object to compare with the current System.CodeDom.Compiler.CompilerInfo.

            Returns: ue if o is a System.CodeDom.Compiler.CompilerInfo object and its value is the same as this instance; otherwise, lse.
        """
        ...
    def GetExtensions(self):
        """
        GetExtensions(self: CompilerInfo) -> Array[str]

            Returns the file name extensions supported by the language provider.

            Returns: An array of file name extensions supported by the language provider.
        """
        ...
    def GetHashCode(self):
        """
        GetHashCode(self: CompilerInfo) -> int

            Returns the hash code for the current instance.

            Returns: A 32-bit signed integer hash code for the current System.CodeDom.Compiler.CompilerInfo instance, suitable for use in hashing algorithms and data structures such as a hash table.
        """
        ...
    def GetLanguages(self):
        """
        GetLanguages(self: CompilerInfo) -> Array[str]

            Gets the language names supported by the language provider.

            Returns: An array of language names supported by the language provider.
        """
        ...
    def __eq__(self, *args):  # cannot find CLR method
        """x.__eq__(y) <==> x==y"""
        ...
    def __ne__(self, *args): ...
    @property
    def CodeDomProviderType(self):
        """
        Gets the type of the configured System.CodeDom.Compiler.CodeDomProvider implementation.

        Get: CodeDomProviderType(self: CompilerInfo) -> Type
        """
        ...
    @property
    def IsCodeDomProviderTypeValid(self):
        """
        Returns a value indicating whether the language provider implementation is configured on the computer.

        Get: IsCodeDomProviderTypeValid(self: CompilerInfo) -> bool
        """
        ...

class CompilerParameters:  # skipped bases: <type 'object'>
    """
    Represents the parameters used to invoke a compiler.

    CompilerParameters()

    CompilerParameters(assemblyNames: Array[str])

    CompilerParameters(assemblyNames: Array[str], outputName: str)

    CompilerParameters(assemblyNames: Array[str], outputName: str, includeDebugInformation: bool)
    """

    @property
    def CompilerOptions(self):
        """
        Gets or sets optional command-line arguments to use when invoking the compiler.

        Get: CompilerOptions(self: CompilerParameters) -> str

        Set: CompilerOptions(self: CompilerParameters) = value
        """
        ...
    @property
    def CoreAssemblyFileName(self):
        """
        Gets or sets the name of the core or standard assembly that contains basic types such as System.Object, System.String, or System.Int32.

        Get: CoreAssemblyFileName(self: CompilerParameters) -> str

        Set: CoreAssemblyFileName(self: CompilerParameters) = value
        """
        ...
    @property
    def EmbeddedResources(self):
        """
        Gets the .NET Framework resource files to include when compiling the assembly output.

        Get: EmbeddedResources(self: CompilerParameters) -> StringCollection
        """
        ...
    @property
    def Evidence(self):
        """
        Specifies an evidence object that represents the security policy permissions to grant the compiled assembly.

        Get: Evidence(self: CompilerParameters) -> Evidence

        Set: Evidence(self: CompilerParameters) = value
        """
        ...
    @property
    def GenerateExecutable(self):
        """
        Gets or sets a value indicating whether to generate an executable.

        Get: GenerateExecutable(self: CompilerParameters) -> bool

        Set: GenerateExecutable(self: CompilerParameters) = value
        """
        ...
    @property
    def GenerateInMemory(self):
        """
        Gets or sets a value indicating whether to generate the output in memory.

        Get: GenerateInMemory(self: CompilerParameters) -> bool

        Set: GenerateInMemory(self: CompilerParameters) = value
        """
        ...
    @property
    def IncludeDebugInformation(self):
        """
        Gets or sets a value indicating whether to include debug information in the compiled executable.

        Get: IncludeDebugInformation(self: CompilerParameters) -> bool

        Set: IncludeDebugInformation(self: CompilerParameters) = value
        """
        ...
    @property
    def LinkedResources(self):
        """
        Gets the .NET Framework resource files that are referenced in the current source.

        Get: LinkedResources(self: CompilerParameters) -> StringCollection
        """
        ...
    @property
    def MainClass(self):
        """
        Gets or sets the name of the main class.

        Get: MainClass(self: CompilerParameters) -> str

        Set: MainClass(self: CompilerParameters) = value
        """
        ...
    @property
    def OutputAssembly(self):
        """
        Gets or sets the name of the output assembly.

        Get: OutputAssembly(self: CompilerParameters) -> str

        Set: OutputAssembly(self: CompilerParameters) = value
        """
        ...
    @property
    def ReferencedAssemblies(self):
        """
        Gets the assemblies referenced by the current project.

        Get: ReferencedAssemblies(self: CompilerParameters) -> StringCollection
        """
        ...
    @property
    def TempFiles(self):
        """
        Gets or sets the collection that contains the temporary files.

        Get: TempFiles(self: CompilerParameters) -> TempFileCollection

        Set: TempFiles(self: CompilerParameters) = value
        """
        ...
    @property
    def TreatWarningsAsErrors(self):
        """
        Gets or sets a value indicating whether to treat warnings as errors.

        Get: TreatWarningsAsErrors(self: CompilerParameters) -> bool

        Set: TreatWarningsAsErrors(self: CompilerParameters) = value
        """
        ...
    @property
    def UserToken(self):
        """
        Gets or sets the user token to use when creating the compiler process.

        Get: UserToken(self: CompilerParameters) -> IntPtr

        Set: UserToken(self: CompilerParameters) = value
        """
        ...
    @property
    def WarningLevel(self):
        """
        Gets or sets the warning level at which the compiler aborts compilation.

        Get: WarningLevel(self: CompilerParameters) -> int

        Set: WarningLevel(self: CompilerParameters) = value
        """
        ...
    @property
    def Win32Resource(self):
        """
        Gets or sets the file name of a Win32 resource file to link into the compiled assembly.

        Get: Win32Resource(self: CompilerParameters) -> str

        Set: Win32Resource(self: CompilerParameters) = value
        """
        ...

class CompilerResults:  # skipped bases: <type 'object'>
    """
    Represents the results of compilation that are returned from a compiler.

    CompilerResults(tempFiles: TempFileCollection)
    """

    @property
    def CompiledAssembly(self):
        """
        Gets or sets the compiled assembly.

        Get: CompiledAssembly(self: CompilerResults) -> Assembly

        Set: CompiledAssembly(self: CompilerResults) = value
        """
        ...
    @property
    def Errors(self):
        """
        Gets the collection of compiler errors and warnings.

        Get: Errors(self: CompilerResults) -> CompilerErrorCollection
        """
        ...
    @property
    def Evidence(self):
        """
        Indicates the evidence object that represents the security policy permissions of the compiled assembly.

        Get: Evidence(self: CompilerResults) -> Evidence

        Set: Evidence(self: CompilerResults) = value
        """
        ...
    @property
    def NativeCompilerReturnValue(self):
        """
        Gets or sets the compiler's return value.

        Get: NativeCompilerReturnValue(self: CompilerResults) -> int

        Set: NativeCompilerReturnValue(self: CompilerResults) = value
        """
        ...
    @property
    def Output(self):
        """
        Gets the compiler output messages.

        Get: Output(self: CompilerResults) -> StringCollection
        """
        ...
    @property
    def PathToAssembly(self):
        """
        Gets or sets the path of the compiled assembly.

        Get: PathToAssembly(self: CompilerResults) -> str

        Set: PathToAssembly(self: CompilerResults) = value
        """
        ...
    @property
    def TempFiles(self):
        """
        Gets or sets the temporary file collection to use.

        Get: TempFiles(self: CompilerResults) -> TempFileCollection

        Set: TempFiles(self: CompilerResults) = value
        """
        ...

class Executor:  # skipped bases: <type 'object'>
    """Provides command execution functions for invoking compilers. This class cannot be inherited."""

    @staticmethod
    def ExecWait(cmd, tempFiles):
        """
        ExecWait(cmd: str, tempFiles: TempFileCollection)

            Executes the command using the specified temporary files and waits for the call to return.

            cmd: The command to execute.

            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to intermediate files generated during compilation.
        """
        ...
    @staticmethod
    def ExecWaitWithCapture(*__args):
        """
        ExecWaitWithCapture(cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)

            Executes the specified command using the specified temporary files and waits for the call to return, storing output and error information from the compiler in the specified strings.

            cmd: The command to execute.

            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to intermediate files generated during compilation.

            outputName: A reference to a string that will store the compiler's message output.

            errorName: A reference to a string that will store the name of the error or errors encountered.

            Returns: The return value from the compiler.

        ExecWaitWithCapture(cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)

            Executes the specified command using the specified current directory and temporary files, and waits for the call to return, storing output and error information from the compiler in the specified strings.

            cmd: The command to execute.

            currentDir: The current directory.

            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to intermediate files generated during compilation.

            outputName: A reference to a string that will store the compiler's message output.

            errorName: A reference to a string that will store the name of the error or errors encountered.

            Returns: The return value from the compiler.

        ExecWaitWithCapture(userToken: IntPtr, cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)

            Executes the specified command using the specified user token and temporary files, and waits for the call to return, storing output and error information from the compiler in the specified strings.

            userToken: The token to start the compiler process with.

            cmd: The command to execute.

            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to intermediate files generated during compilation.

            outputName: A reference to a string that will store the compiler's message output.

            errorName: A reference to a string that will store the name of the error or errors encountered.

            Returns: The return value from the compiler.

        ExecWaitWithCapture(userToken: IntPtr, cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)

            Executes the specified command using the specified user token, current directory, and temporary files; then waits for the call to return, storing output and error information from the compiler in the specified strings.

            userToken: The token to start the compiler process with.

            cmd: The command to execute.

            currentDir: The directory to start the process in.

            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to intermediate files generated during compilation.

            outputName: A reference to a string that will store the compiler's message output.

            errorName: A reference to a string that will store the name of the error or errors encountered.

            Returns: The return value from the compiler.
        """
        ...
    __all__ = [
        "ExecWait",
        "ExecWaitWithCapture",
    ]

class GeneratedCodeAttribute(Attribute):  # skipped bases: <type '_Attribute'>
    """
    Identifies code generated by a tool. This class cannot be inherited.

    GeneratedCodeAttribute(tool: str, version: str)
    """

    @staticmethod  # known case of __new__
    def __new__(cls, tool, version):
        """__new__(cls: type, tool: str, version: str)"""
        ...
    @property
    def Tool(self):
        """
        Gets the name of the tool that generated the code.

        Get: Tool(self: GeneratedCodeAttribute) -> str
        """
        ...
    @property
    def Version(self):
        """
        Gets the version of the tool that generated the code.

        Get: Version(self: GeneratedCodeAttribute) -> str
        """
        ...

class GeneratorSupport(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines identifiers used to determine whether a code generator supports certain types of code elements.

    enum (flags) GeneratorSupport, values: ArraysOfArrays (1), AssemblyAttributes (4096), ChainedConstructorArguments (32768), ComplexExpressions (524288), DeclareDelegates (512), DeclareEnums (256), DeclareEvents (2048), DeclareIndexerProperties (33554432), DeclareInterfaces (1024), DeclareValueTypes (128), EntryPointMethod (2), GenericTypeDeclaration (16777216), GenericTypeReference (8388608), GotoStatements (4), MultidimensionalArrays (8), MultipleInterfaceMembers (131072), NestedTypes (65536), ParameterAttributes (8192), PartialTypes (4194304), PublicStaticMembers (262144), ReferenceParameters (16384), Resources (2097152), ReturnTypeAttributes (64), StaticConstructors (16), TryCatchStatements (32), Win32Resources (1048576)
    """

    ArraysOfArrays = None
    AssemblyAttributes = None
    ChainedConstructorArguments = None
    ComplexExpressions = None
    DeclareDelegates = None
    DeclareEnums = None
    DeclareEvents = None
    DeclareIndexerProperties = None
    DeclareInterfaces = None
    DeclareValueTypes = None
    EntryPointMethod = None
    GenericTypeDeclaration = None
    GenericTypeReference = None
    GotoStatements = None
    MultidimensionalArrays = None
    MultipleInterfaceMembers = None
    NestedTypes = None
    ParameterAttributes = None
    PartialTypes = None
    PublicStaticMembers = None
    ReferenceParameters = None
    Resources = None
    ReturnTypeAttributes = None
    StaticConstructors = None
    TryCatchStatements = None
    value__ = None
    Win32Resources = None

class ICodeParser:
    """Defines an interface for parsing code into a System.CodeDom.CodeCompileUnit."""

    def Parse(self, codeStream):
        """
        Parse(self: ICodeParser, codeStream: TextReader) -> CodeCompileUnit

            When implemented in a derived class, compiles the specified text stream into a System.CodeDom.CodeCompileUnit.

            codeStream: A System.IO.TextReader that can be used to read the code to be compiled.

            Returns: A System.CodeDom.CodeCompileUnit that contains a representation of the parsed code.
        """
        ...

class IndentedTextWriter(TextWriter):  # skipped bases: <type 'IDisposable'>
    """
    Provides a text writer that can indent new lines by a tab string token.

    IndentedTextWriter(writer: TextWriter)

    IndentedTextWriter(writer: TextWriter, tabString: str)
    """

    def OutputTabs(self, *args):  # cannot find CLR method
        """
        OutputTabs(self: IndentedTextWriter)

            Outputs the tab string once for each level of indentation according to the System.CodeDom.Compiler.IndentedTextWriter.Indent property.
        """
        ...
    def WriteLineNoTabs(self, s):
        """
        WriteLineNoTabs(self: IndentedTextWriter, s: str)

            Writes the specified string to a line without tabs.

            s: The string to write.
        """
        ...
    @property
    def Encoding(self):
        """
        Gets the encoding for the text writer to use.

        Get: Encoding(self: IndentedTextWriter) -> Encoding
        """
        ...
    @property
    def Indent(self):
        """
        Gets or sets the number of spaces to indent.

        Get: Indent(self: IndentedTextWriter) -> int

        Set: Indent(self: IndentedTextWriter) = value
        """
        ...
    @property
    def InnerWriter(self):
        """
        Gets the System.IO.TextWriter to use.

        Get: InnerWriter(self: IndentedTextWriter) -> TextWriter
        """
        ...
    @property
    def NewLine(self):
        """
        Gets or sets the new line character to use.

        Get: NewLine(self: IndentedTextWriter) -> str

        Set: NewLine(self: IndentedTextWriter) = value
        """
        ...
    CoreNewLine = None
    DefaultTabString = "    "

class LanguageOptions(Enum):  # skipped bases: <type 'IComparable'>, <type 'IConvertible'>, <type 'IFormattable'>
    """
    Defines identifiers that indicate special features of a language.

    enum (flags) LanguageOptions, values: CaseInsensitive (1), None (0)
    """

    CaseInsensitive = None
    value__ = None

class TempFileCollection(ICollection, IDisposable):  # skipped bases: <type 'IEnumerable'>
    """
    Represents a collection of temporary files.

    TempFileCollection()

    TempFileCollection(tempDir: str)

    TempFileCollection(tempDir: str, keepFiles: bool)
    """

    def AddExtension(self, fileExtension, keepFile=None):
        """
        AddExtension(self: TempFileCollection, fileExtension: str) -> str

            Adds a file name with the specified file name extension to the collection.

            fileExtension: The file name extension for the auto-generated temporary file name to add to the collection.

            Returns: A file name with the specified extension that was just added to the collection.

        AddExtension(self: TempFileCollection, fileExtension: str, keepFile: bool) -> str

            Adds a file name with the specified file name extension to the collection, using the specified value indicating whether the file should be deleted or retained.

            fileExtension: The file name extension for the auto-generated temporary file name to add to the collection.

            keepFile: ue if the file should be kept after use; lse if the file should be deleted.

            Returns: A file name with the specified extension that was just added to the collection.
        """
        ...
    def AddFile(self, fileName, keepFile):
        """
        AddFile(self: TempFileCollection, fileName: str, keepFile: bool)

            Adds the specified file to the collection, using the specified value indicating whether to keep the file after the collection is disposed or when the System.CodeDom.Compiler.TempFileCollection.Delete method is called.

            fileName: The name of the file to add to the collection.

            keepFile: ue if the file should be kept after use; lse if the file should be deleted.
        """
        ...
    def Delete(self):
        """
        Delete(self: TempFileCollection)

            Deletes the temporary files within this collection that were not marked to be kept.
        """
        ...
    def GetEnumerator(self):
        """
        GetEnumerator(self: TempFileCollection) -> IEnumerator

            Gets an enumerator that can enumerate the members of the collection.

            Returns: An System.Collections.IEnumerator that contains the collection's members.
        """
        ...
    def __len__(self, *args):  # cannot find CLR method
        """x.__len__() <==> len(x)"""
        ...
    @property
    def BasePath(self):
        """
        Gets the full path to the base file name, without a file name extension, on the temporary directory path, that is used to generate temporary file names for the collection.

        Get: BasePath(self: TempFileCollection) -> str
        """
        ...
    @property
    def Count(self):
        """
        Gets the number of files in the collection.

        Get: Count(self: TempFileCollection) -> int
        """
        ...
    @property
    def KeepFiles(self):
        """
        Gets or sets a value indicating whether to keep the files, by default, when the System.CodeDom.Compiler.TempFileCollection.Delete method is called or the collection is disposed.

        Get: KeepFiles(self: TempFileCollection) -> bool

        Set: KeepFiles(self: TempFileCollection) = value
        """
        ...
    @property
    def TempDir(self):
        """
        Gets the temporary directory to store the temporary files in.

        Get: TempDir(self: TempFileCollection) -> str
        """
        ...

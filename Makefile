#SOURCES=./KickassUndelete/ConsoleCommands.cs ./KickassUndelete/DeletedFileViewer.cs ./KickassUndelete/DeletedFileViewer.Designer.cs ./KickassUndelete/ExtensionInfo.cs ./KickassUndelete/ExtensionMethods.cs ./KickassUndelete/FileSavingQueue.cs ./KickassUndelete/ListViewColumnSorter.cs ./KickassUndelete/ListViewNoFlicker.cs ./KickassUndelete/MainForm.cs ./KickassUndelete/MainForm.Designer.cs ./KickassUndelete/Program.cs ./KickassUndelete/Properties/AssemblyInfo.cs ./KickassUndelete/Properties/Resources.Designer.cs ./KickassUndelete/Properties/Settings.Designer.cs ./KickassUndelete/ScanState.cs
SOURCES=KickassUndelete/*.cs KickassUndelete/*/*.cs
LIBS=FileSystems/KFA.FileSystems.Lite.dll GuiComponents/KFA.GuiComponents.dll
RESOURCES=KickassUndelete/DeletedFileViewer.resources KickassUndelete/MainForm.resources KickassUndelete/Properties/Resources.resx
.SUFFIXES:
.SUFFIXES: .resx .resources
.resx.resources:
	resgen $<
KickassUndelete.exe: ${LIBS} ${SOURCES} ${RESOURCES}
	make -C FileSystems
	make -C GuiComponents
	mcs -d:MONO -o KickassUndelete.exe -r:System.Drawing.dll -r:System.Windows.Forms.dll -r:System.Data.dll $(addprefix -r:,${LIBS}) $(addprefix -resource:,${RESOURCES}) ${SOURCES}
clean:
	rm KickassUndelete.exe

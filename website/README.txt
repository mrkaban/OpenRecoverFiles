==================================================
Kickass Undelete Release Notes
==================================================

Version 1.5.4 - 2017-12-08
Changes:
 * Fixed a crash when trying to load a file path containing invalid characters.

Version 1.5.3 - 2017-10-01
Changes:
 * Fixed a crash when parent directories had no recoverable filename

Version 1.5.2
Changes:
 * Fixed crashes on Windows 8
 
Version 1.5.1
Changes:
 * Fixed startup crash on Windows XP
 * Removed beta label

Version 1.5 beta
Changes:
 * Better estimation of recovery chances for both FAT and NTFS
 * Fixed a bug that was causing some FAT files to be recovered incorrectly
 * Show the drive letter in file paths
 * Replace paths that are clearly incorrect with a "?"
 * Performance improvements in long lists of files
 * Now requires only the .NET 4.0 Client Profile
 * Allow user to save selected files if no files are checked
 * Remove invalid characters from FAT filenames

Version 1.4 beta
Changes:
 * Allow running from command line
 * Show file paths in the list of deleted files
 * Scanning performance improvements
 * List filtering performance improvements
 * Now warns before saving a file to the same drive it's being recovered from
 * Fixed an NTFS crashing bug
 * Open Windows Explorer to the location of a recovered file after recovery is complete
 * Provide the option to run as admin on startup
 * Allow more files to be recovered while recovery is running
 * When recovering files, don't replace existing files
 * Make sure recovered file names are valid

Version 1.3 beta
Changes:
 * Added a "Chance of Recovery" estimation for NTFS drives
 * Added an automatic filter of system and unknown files.
 * Fixed a bug where Undelete crashed if admin rights weren't granted.

Version 1.2 beta
Changes:
 * Fixed some annoying UI errors
 * Only show deleted files in the list (not folders)
 * Allow filter text matching on the file type as well as the name

Version 1.1 beta
Changes:
 * Fixed a number of bugs in FAT support
 * Fixed some threading bugs
 * Performance improvements
 * File type icons
 * Friendly file type descriptions
 * Date modified
 * Scans on FAT drives now estimate progress properly

Version: 1.0 beta
Initial release, supporting:
 * NTFS support
 * Basic FAT support
 * Recovery of deleted files
 * Filter file list by name and extension
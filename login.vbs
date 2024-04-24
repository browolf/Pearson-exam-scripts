Set objShell = WScript.CreateObject("WScript.Shell")
Dim fso, msg
Set fso = CreateObject("Scripting.FileSystemObject")
Set objNetwork = CreateObject("WScript.Network") 
Set lso = CreateObject("Scripting.FileSystemObject")
Const ForAppending = 8

strComputerName = objShell.ExpandEnvironmentStrings( "%COMPUTERNAME%" )
' 29/11/13 turned error checking off for line 32 to fix w: not working in k3

Do until completed=true 
foldername = ""
Do until foldername>""
foldername=inputbox ("Enter Code", "Controlled Assessments")

loop
   
fldr = "\\pupil\assessments$\" & foldername

'Remove drive mappings.  
If (fso.FolderExists("S:\")) Then objNetwork.RemoveNetworkDrive "S:"
If (fso.FolderExists("w:\")) Then objNetwork.RemoveNetworkDrive "W:"

'map pseudo w: drive
on error resume next
'If (fso.FolderExists("\\pupil\subjects$\assessments")) Then  
objNetwork.MapNetworkDrive "w:", "\\pupil\subjects$\assessments"
on error goto 0
 
 
'map s: drive to folder inputted code
   If (fso.FolderExists(fldr)) Then 
		objNetwork.MapNetworkDrive "S:", "\\pupil\assessments$\"&foldername
	  
	  If (fso.FolderExists("S:\")) Then 
		ret=msgbox("Userarea connected", 64)
         completed=true
				'log code & computer
				fname=foldername & ".txt"
				'ret=msgbox("\\dev\logs$\assessment\" & fname, 64)
				Set ts = fso.OpenTextFile("\\dev\logs$\assessment\" & fname, ForAppending, True)
				ts.writeline(strComputerName & "," & date & "," & time)
	  else 
	    'if there was an unspeciffied error
		ret=msgbox("Userarea failed - Call your teacher! ", 48) 
                completed=false
      end if
	  'if they typed the code in wrong
   Elseif (fso.FolderExists(fldr) <> true) then
      ret=msgbox("Code not found, you typed it in wrong!",48)
      completed=false
  End If


loop

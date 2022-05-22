from paramiko import SSHClient, AutoAddPolicy # SSH remote command to activate the host machine control
with SSHClient() as client:
                     client.set_missing_host_key_policy(AutoAddPolicy())
                     #print(robothostname)
                     #print(hostip_mem[0],robothostname[0],host_password[0])
                     client.connect(hostname="192.168.50.216",username="pi",password="Rkl3548123#",look_for_keys=False) #Getting all the data from the host ip,host_name and the other hostmachine to connect 
                     command = ["ls","python3 wifiscanner.py","lsusb"]
                     #Access remote command with sodo combine password generated working 
                     #Fix your host password into the remote machine password
                     run_com = ["export DISPLAY=:0","python3 Sensor_array_robot_lib.py"]
                     try:
                        print("Remote chmod permission")
                        #for r in run_com:
                        
                        try:
                            
                              stdin, stdout, stderr = client.exec_command(str(run_com[0])+"&&"+str(run_com[1]),get_pty=True)
                              lines = stdout.readlines() 
                              print(lines)
                              stdin.close()

                        except:
                               print("Error calling data")
                           #lines = stdout.readlines()
                           #print(lines)
                         #Messagebox here to display the progress bar 
                        
                         #msgbox = QtWidgets.QMessageBox()
                         #msgbox.setText('Finish robogenerator firmware generated')
                         #msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) # (QtCore.Qt.TextSelectableByMouse)
                         #stdin, stdout, stderr = client.exec_command(command[0],get_pty=True)
                         #lines = stdout.readlines()
                         #print(lines)
                         #print(lines[0])
                         #for dataremote in range(0,len(lines)):   
                         #     msgbox.setDetailedText(lines[dataremote]+"\n")
                         #msgbox.exec() 
                         #From the lines output list array seeking the cannot access as the trigger word for git installation on the system to prepare the remote firmware installation process 
                         #Reding the bash script in the list array to modify the firmware percentage report firmware installation progress 
                     except:
                         print("Remote chmod permission fail")
                     
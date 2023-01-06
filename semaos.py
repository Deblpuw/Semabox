import dialog
import subprocess


def execute_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        # La commande s'est exécutée avec succès
        output = result.stdout.decode()
    else:
        # La commande a échoué
        output = result.stderr.decode()
    return output




def action_1():
    command_result = execute_command(["ip", "a"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)


def action_2():
    command_result = execute_command(["curl", "ifconfig.me"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result)

#def action_3():
#    command_result = execute_command(["ip", "route", "|", "grep", "src", "|", "awk", "'{print $1}'", "|", "tee", "tmp"])
#    process1 = subprocess.Popen(["ip", "route"], stdout=subprocess.PIPE)
#    process2 = subprocess.Popen(["grep", "src"], stdin=process1.stdout, stdout=subprocess.PIPE)
#    process3 = subprocess.Popen(["awk", "'{print $1}'"], stdin=process2.stdout, stdout=subprocess.PIPE)
#    process4 = subprocess.Popen(["tee", "tmp"], stdin=process3.stdout, stdout=subprocess.PIPE)

#    process4.wait()
#    output = process4.stdout.decode()
#    print(output)
#with open("tmp", "w") as f:
#    f.write(output.decode())
    

#    commands_result = execute_command(["nmap", "-sn", "-iL", "tmp"])
#    result = execute_command(["cat", "tmps"])
#    d = dialog.Dialog(dialog="dialog")
#    d.msgbox(text=result)


#def action_3():
#    command_result = execute_command(["ip", "route", "|", "grep", "src", "|", "awk", "'{print $1}'>", "tmp"])
#    command_result = subprocess.run(["nmap", "-sn", "-iL", "tmp"],stdout=subprocess.PIPE, input=command_result.stdout )
#    result = command_result.stdout.decode()
#    d = dialog.Dialog(dialog="dialog")
#    d.msgbox(text=result)

def action_4():
    command_result = execute_command(["less", "./networkinfo.log"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)

def action_5():
    command_result = execute_command(["fast", "-u", ">", "debit.txt"])
    result = execute_command(["tail", "-n", "3", "debit.txt"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=result)

def action_6():
    command_result = execute_command(["git", "log", "-1"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)

def action_7():
    command_result = execute_command(["git", "stash", "&&", "git", "pull", "origin", "main"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)


actions = {"1": action_1,
           "2": action_2,
           "3": action_3,
           "4": action_4,
           "5": action_5,
           "6": action_6,
           "7": action_7}

d = dialog.Dialog(dialog="dialog")

code, tag = d.menu("Selectionnez une action",
                   choices=[("1", "Mon IP Privé"),
                            ("2", "Mon IP Publique"),
                            ("3", "Scan de Réseau"),
                            ("4", "Test de connexion"),
                            ("5", "Test de débit"),
                            ("6", "Version"),
                            ("7", "Mise a jour")],

                   title="Bienvenu sur SemaOS")

if code == d.OK:
    actions[tag]()

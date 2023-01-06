mport dialog
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


def action_3():
    command_result = execute_command(["ip"," route", "|", "grep", "src", "|", "grep", "eth0", "|", "awk", "'{print $1}'", ">", "tmp"], stdout=subprocess.PIPE)
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)

def action_4():
    command_result = execute_command(["ip", "a"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)
    
def action_5():
    command_result = execute_command(["ip", "a"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)

def action_6():
    command_result = execute_command(["ip", "a"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)

def action_7():
    command_result = execute_command(["ip", "a"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result, height=80, width=80)

actions = {"1": action_1,
           "2": action_2,
           "3": action_3}

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


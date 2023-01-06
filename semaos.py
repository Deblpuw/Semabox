
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
    command_result = execute_command(["ip", "a","|","grep" ,l])
    d = dialog.Dialog(dialog="dialog")
    d.programbox(command_result)

def action_2():
    result = subprocess.run(["curl", "ifconfig.me"],stdout=subprocess.PIPE)
    d = dialog.Dialog(dialog="dialog")
    d.programbox(result.stdout.decode())

def action_3():
    result = subprocess.run(["ip"," route", "|", "grep", "src", "|", "grep", "eth0", "|", "awk", "'{print $1}'", ">", "tmp"], stdout=subprocess.PIPE)
    d = dialog.Dialog(dialog="dialog")
    d.programbox("Resultat", result.stdout.decode())



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


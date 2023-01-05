import dialog

import subprocess


#def action_1():
#    result = subprocess.run(["ip a"], stdout=subprocess.PIPE)
#    d = dialog.Dialog(dialog="dialog")
#    d.programbox("Resultat", result.stdout.decode())
    
def execute_command(command):
   result = subprocess.run(command, stdout=subprocess.PIPE)
   return result.stdout.decode()
   
#def action_3():
#    print("Option 3 sélectionnée. Exécution de l'action correspondante.")

#actions = {"1": action_1,
#           "2": action_2,
#           "3": action_3}

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
#    actions[tag]()
    if tag == "1":
        command_result = execute_command(["ip", "a"])
        d.programbox(command_result, "Resultat")

    elif tag == "2":
        command_result = execute_command(["curl", "ifconfig.me"])
        d.programbox(command_result, "Resultat")


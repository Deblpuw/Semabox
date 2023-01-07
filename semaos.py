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
    interfaces = netifaces.interfaces()
    for i in interfaces:
        iface_data = netifaces.ifaddresses(i)
        if netifaces.AF_INET in iface_data:
            ip_address = iface_data[netifaces.AF_INET][0]['addr']
            ip = f"Adresse IP de l'interface {i}: {ip_address}"    
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=ip)


def action_2():
    command_result = execute_command(["curl", "ifconfig.me"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result)

def action_3():
    process1 = subprocess.Popen(["ip", "route"], stdout=subprocess.PIPE)
    process2 = subprocess.Popen(["grep", "src"], stdin=process1.stdout, stdout=subprocess.PIPE)
    process3 = subprocess.Popen(["awk", "{print $1}"], stdin=process2.stdout, stdout=subprocess.PIPE)

    process4 = subprocess.Popen(["tee", "tmp"], stdin=process3.stdout, stdout=subprocess.PIPE)
    process4.wait()
    output = process4.communicate()[0].decode()
    with open("tmp", "w") as f:
        f.write(output)

    process5 = subprocess.Popen(["nmap", "-sn", "-iL", "tmp"], stdout=subprocess.PIPE)
    process6 = subprocess.CompletedProcess(["tee", "tmps"], stdin=process5.stdout, stdout=subprocess.PIPE)

    process6.wait()
    output = process6.stdout.decode()
    with open("tmps", "w") as f:
        f.write(output)

    result = execute_command(["cat", "tmps"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=result)

def action_4():
    command_result = execute_command(["less", "./networkinfo.log"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result)

def action_5():
    command_result = execute_command(["fast", "-u", ">", "debit.txt"])
    result = execute_command(["tail", "-n", "3", "debit.txt"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=result)

def action_6():
    command_result = execute_command(["git", "log", "-1"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result)

def action_7():
    command_result = execute_command(["git", "stash", "&&", "git", "pull", "origin", "main"])
    d = dialog.Dialog(dialog="dialog")
    d.msgbox(text=command_result)


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

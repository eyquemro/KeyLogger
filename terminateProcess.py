import os
import psutil

# Lire le PID du fichier
pid_file = "pid.txt"
if os.path.exists(pid_file):
    with open(pid_file, "r") as file:
        pid = int(file.read().strip())

    # Trouver le processus et le tuer
    if psutil.pid_exists(pid):
        try:
            process = psutil.Process(pid)
            process.terminate()  # ou process.kill() pour tuer immédiatement
            process.wait(timeout=5)  # Attendre que le processus se termine
            print(f"Process {pid} terminated.")
            os.remove(pid_file)  # Supprimer le fichier PID si le processus est terminé
        except psutil.TimeoutExpired:
            print(f"Process {pid} did not terminate in time.")
        except psutil.NoSuchProcess:
            print(f"Process {pid} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"Process {pid} does not exist.")
else:
    print("PID file not found.")

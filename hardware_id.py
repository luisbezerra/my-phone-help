import subprocess
import hashlib

def get_hwid():
    # Executa comando do Windows para pegar o Serial Único da Placa-mãe
    cmd = 'wmic csproduct get uuid'
    try:
        uuid = subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
        # Transformamos em um Hash SHA256 para segurança (não enviar o dado puro)
        return hashlib.sha256(uuid.encode()).hexdigest()
    except Exception as e:
        return f"Erro_ao_capturar_ID: {e}"

if __name__ == "__main__":
    print(f"O ID Único deste PC é: {get_hwid()}")

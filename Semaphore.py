import threading
import time

reciptionist = threading.Semaphore(1)

def enter_examinationroom(n):
    print(f"patient {n} is waiting for his turn")
    reciptionist.acquire()
    print(f"patient {n} is in the examination room")
    time.sleep(2)
    print(f"patient {n} is out of the examination room")
    reciptionist.release()

patients = []
for i in range(5):
    Patient = threading.Thread(target=enter_examinationroom,args=(i,))
    patients.append(Patient)
    Patient.start()







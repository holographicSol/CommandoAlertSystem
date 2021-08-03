'''
WRITTEN BY HOLOGRAPHIC_SOL AKA BENJAMIN JACK CULLEN
This program is designed to alert when non-commercial aircraft enters into proximity.
'''

import subprocess
import sys
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
##speaker.Speak('activating commando alert system.')

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

cmd = 'dump1090.bat'
xcmd = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

count = 0
last_lne = ''
while True:
    output = xcmd.stdout.readline()
    last_lne = output
    if output == '' and xcmd.poll() is not None:
        break
    if output:
        try:
            op = output.decode("utf-8").strip()
            op = op.replace('Hex     Mode  Sqwk  Flight   Alt    Spd  Hdg    Lat      Long   Sig  Msgs   Ti-', '')
            op = op.replace('Hex     Mode  Sqwk  Flight   Alt    Spd  Hdg    Lat      Long   Sig  Msgs   Ti/', '')
            op = op.replace('Hex     Mode  Sqwk  Flight   Alt    Spd  Hdg    Lat      Long   Sig  Msgs   Ti|', '')
            op = op.replace('Hex     Mode  Sqwk  Flight   Alt    Spd  Hdg    Lat      Long   Sig  Msgs   Ti\\', '')
            op = op.replace('Hex     Mode  Sqwk  Flight   Alt    Spd  Hdg    Lat      Long   Sig  Msgs   Ti|', '')
            op = op.replace('-------------------------------------------------------------------------------', '')
            if not op is None:
                if count > 23 and count <= 24:
                    print('\n\nHex     Mode  Sqwk  Flight   Alt    Spd  Hdg    Lat      Long   Sig  Msgs   Ti')

            print(op)
            if 'CMDO' in op:
                speaker.Speak('commando alert. commando alert' + op)
            elif 'DINGO' in op:
                speaker.Speak('Dingo alert. Dingo alert' + op)
            elif 'AZTEC' in op:
                speaker.Speak('AZTEC alert. AZTEC alert' + op)

        except:
            pass
    count += 1
rc = xcmd.poll()

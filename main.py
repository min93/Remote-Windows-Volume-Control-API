from flask import Flask, request, jsonify
from ctypes import cast, POINTER
from comtypes import CoInitialize, CoUninitialize, CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

client = Flask(__name__)

def set_volume(level):
    CoInitialize()  
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(level / 100, None)
    finally:
        CoUninitialize()  

def get_current_volume():
    CoInitialize()  
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar() * 100
        return current_volume
    finally:
        CoUninitialize()  

@client.route('/set_volume', methods=['POST'])
def api_set_volume():
    level = request.json.get('level')
    set_volume(level)
    return jsonify({"status": "success", "volume_set_to": level})

@client.route('/get_volume', methods=['GET'])
def api_get_volume():
    try:
        current_volume = get_current_volume()
        return jsonify({"status": "success", "current_volume": current_volume})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    client.run(host='0.0.0.0', port=5000)

import subprocess

def run_rasa_server():
    # Specify the path to your Rasa model
    model_path = "chatbot\models\20231202-190337-rectilinear-meter.tar.gz"

    # Command to run the Rasa server in API mode
    command = f"rasa run --enable-api -m {model_path}"

    # Use subprocess to run the Rasa server
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_rasa_server()
# Testing push

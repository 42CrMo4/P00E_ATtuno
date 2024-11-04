import os
import re
import sys

def find_missing_3d_models(project_dir):
    missing_models = []
    kicad_pcb_file = os.path.join(project_dir, "design.kicad_pcb")
    if not os.path.exists(kicad_pcb_file):
        print("Error: project.kicad_pcb not found in the project directory.")
        sys.exit(1)

    with open(kicad_pcb_file, 'r') as f:
        content = f.read()

    # Regular expression to find 3D model paths
    model_pattern = re.compile(r'\(model\s+"([^"]+)"')
    models = model_pattern.findall(content)

    for model in models:
        # Check if the model path starts with ${KIPRJMOD}/3d-models/
        if model.startswith("${KIPRJMOD}/3d-models/"):
            relative_path = model.replace("${KIPRJMOD}/3d-models/", "")
            full_path = os.path.join(project_dir, "3d-models", relative_path)
            if not os.path.exists(full_path):
                missing_models.append(relative_path)

    return missing_models

def main():
    project_dir = os.getcwd()
    missing_models = find_missing_3d_models(project_dir)

    if missing_models:
        print("The following 3D models are missing:")
        for model in missing_models:
            print(f"- {model}")
        sys.exit(1)
    else:
        print("All 3D models are present.")

if __name__ == "__main__":
    main()
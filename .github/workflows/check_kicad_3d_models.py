import os
import re
import sys

def find_kicad_pcb_files(directory):
    """Find all KiCad PCB files in the directory."""
    found_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.kicad_pcb'):
                found_files.append(os.path.join(root, file))
    print(f"\n[DEBUG] Found KiCad PCB files: {found_files}")
    return found_files

def find_missing_3d_models(kicad_pcb_file):
    missing_models = set()
    project_dir = os.path.dirname(kicad_pcb_file)

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
                missing_models.add(relative_path)

    return missing_models

def main():
    project_dir = os.getcwd()
    kicad_pcb_files = find_kicad_pcb_files(project_dir)

    all_missing_models = set()
    for kicad_pcb_file in kicad_pcb_files:
        missing_models = find_missing_3d_models(kicad_pcb_file)
        all_missing_models.update(missing_models)

    if all_missing_models:
        print("The following 3D models are missing:")
        for model in all_missing_models:
            print(f"- {model}")
        sys.exit(1)
    else:
        print("All 3D models are present.")

if __name__ == "__main__":
    main()
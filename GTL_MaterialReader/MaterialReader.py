
import adsk.core
import adsk.fusion
import traceback
import os


def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface

    try:
        # Ruta del archivo de salida
        escritorio = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        ruta = os.path.join(
            escritorio,
            "materiales_fusion.txt"
        )

        with open(ruta, "w", encoding="utf-8") as f:

            # Recorrer bibliotecas
            for lib in app.materialLibraries:

                f.write("\n" + "=" * 60 + "\n")
                f.write(f"BIBLIOTECA: {lib.name}\n")
                f.write("=" * 60 + "\n")

                # Materiales físicos
                f.write("\n--- MATERIALES FÍSICOS ---\n")

                for material in lib.materials:
                    f.write(f"\nMaterial: {material.name}\n")
                    f.write(f"ID: {material.id}\n")

                    # Atributos personalizados
                    try:
                        for attr in material.attributes:
                            f.write(
                                f"Atributo [{attr.groupName}] "
                                f"{attr.name}: {attr.value}\n"
                            )
                    except Exception:
                        f.write("Sin atributos accesibles.\n")

                # Apariencias visuales
                f.write("\n--- APARIENCIAS ---\n")

                for appearance in lib.appearances:
                    f.write(
                        f"Nombre: {appearance.name} | "
                        f"ID: {appearance.id}\n"
                    )

        ui.messageBox(
            "Archivo creado correctamente:\n" + ruta
        )

    except Exception:
        ui.messageBox(
            "Error al generar el archivo:\n\n"
            + traceback.format_exc()
        )

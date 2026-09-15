from organizador import clasificar, organizar_carpeta
def test_clasificar_reconoce_imagen(tmp_path):
 archivo = tmp_path / "foto.jpg"
 archivo.write_text("contenido")
 assert clasificar(archivo) == "Imagenes"
def test_organizar_mueve_archivo_a_subcarpeta(tmp_path):
 archivo = tmp_path / "foto.jpg"
 archivo.write_text("contenido")
 organizar_carpeta(tmp_path)
 assert (tmp_path / "Imagenes" / "foto.jpg").exists()
 assert not archivo.exists()

 
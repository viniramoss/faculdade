package exercicios;

public class Episodios {
    String titulo;
    String duration;

    public Episodios (String titulo, String duration) {
        this.titulo = titulo;
        this.duration = duration;
    }
    public void mostrarInfo() {
        System.out.println("Titulo: " + titulo);
        System.out.println("Duration: " + duration);
    }

    public static void main(String[] args) {
        Episodios episodio1 = new Episodios("Ep1", "20");
        Episodios episodio2 = new Episodios("Ep2", "30");
        Episodios episodio3 = new Episodios("Ep3", "40");
        Episodios episodio4 = new Episodios("Ep4", "50");
        Episodios episodio5 = new Episodios("Ep5", "60");
    }
}

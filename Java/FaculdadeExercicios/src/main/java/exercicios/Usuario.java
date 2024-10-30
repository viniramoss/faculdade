package exercicios;

public class Usuario {
        String nome;
        String email;
        String senha;

        public Usuario (String email, String nome, String senha) {
            this.email = email;
            this.nome = nome;
            this.senha = senha;
        }
        public void mostrarInfo () {
            System.out.println("Email: "+ email);
            System.out.println("Nome: "+ nome);
        }
        public boolean verificarSenha (String senhaInformada) {
            return this.senha.equals(senhaInformada);
        }
    public static void main(String[] args) {
        Usuario usuario1 = new Usuario("vini@gmail.com", "Vinicius Ramos", "alovini123");
        boolean senhaCorreta = usuario1.verificarSenha("alovini123");
        System.out.println(senhaCorreta);
        boolean senhaIncorreta = usuario1.verificarSenha("aalovini123");
        System.out.println(senhaIncorreta);
    }
}

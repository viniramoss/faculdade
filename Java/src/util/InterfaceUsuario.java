package util;
import java.util.Scanner;

public class InterfaceUsuario {
    private Scanner scanner = new Scanner(System.in);
    private int prazo;
    private double taxa;
    private double valor;

    public int getPrazoEmAnos() {
        do {
            System.out.println("Digite o prazo em anos: ");
            prazo = scanner.nextInt();
            if (prazo <= 0) {
                System.out.println("Erro: O prazo deve ser maior que zero anos!");
            }
        } while (prazo <= 0);
        return prazo;

    }

    public double getTaxaDeJurosAnual() {
        do {
            System.out.println("Digite a taxa de juros anual: ");
            taxa = scanner.nextDouble();
            if (taxa < 0 || taxa > 500) {
                System.out.println("Erro: taxa muito baixa ou muito alta!");
            }
        } while (taxa < 0 || taxa > 500);
        return taxa;
    }

    public double getValorDoImovel() {
        do {
            System.out.println("Digite o valor do imovel: ");
            valor = scanner.nextDouble();
            if(valor <= 0) {
                System.out.println("Erro: Valor nao pode ser negativo!");
            }
        } while (valor <= 0);
        return valor;
    }

    public void fecharScanner() {
        scanner.close();
    }
}
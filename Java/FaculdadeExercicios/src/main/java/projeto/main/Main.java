package projeto.main;

import projeto.modelo.Financiamento;
import projeto.util.InterfaceUsuario;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        ArrayList<Financiamento> financiamentos = new ArrayList<>();
        boolean adicionarOutro = true;

        while (adicionarOutro) {
            System.out.println("\n--- Adicionando Novo Financiamento ---");

            double valorImovel = interfaceUsuario.getValorDoImovel();
            double taxaDeJurosAnual = interfaceUsuario.getTaxaDeJurosAnual();
            int prazoEmAnos = interfaceUsuario.getPrazoEmAnos();

            Financiamento financiamento = new Financiamento(valorImovel, prazoEmAnos, taxaDeJurosAnual);
            financiamento.calcularPagamentoMensal();
            financiamento.calcularTotalDoPagamento();

            financiamentos.add(financiamento);

            System.out.print("Deseja adicionar outro financiamento?  Digite s | n: ");
            String resposta = scanner.next();
            adicionarOutro = resposta.equalsIgnoreCase("s");
        }

        System.out.println("\n--- Seus Financiamentos ---");
/*
        for (int i = 0; i < financiamentos.size(); i++) {
            financiamentos.get(i).mostrarResultados();
            System.out.println("---------------------");
        }
*/
        for (Financiamento financiamento : financiamentos) {
            financiamento.mostrarResultados();
            System.out.println("---------------------");
        }
        interfaceUsuario.fecharScanner();
        scanner.close();
    }
}
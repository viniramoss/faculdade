package main;

import modelo.Financiamento;
import util.InterfaceUsuario;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        ArrayList<Financiamento> financiamentos = new ArrayList<>();


        financiamentos.add(new Financiamento(200000, 20, 10));
        financiamentos.add(new Financiamento(150000, 15, 9.5));
        financiamentos.add(new Financiamento(100000, 10, 8.5));

//        aqui coloquei o codigo para adicionar pelo menos 3 finciamentos como default

        for (Financiamento f : financiamentos) {
            f.calcularPagamentoMensal();
            f.calcularTotalDoPagamento();
        }

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

            System.out.print("Deseja adicionar outro financiamento? Digite s | n: ");
            String resposta = scanner.next();
            adicionarOutro = resposta.equalsIgnoreCase("s");
        }

        System.out.println("\n--- Seus Financiamentos ---");
        for (Financiamento financiamento : financiamentos) {
            financiamento.mostrarResultados();
            System.out.println("---------------------");
        }
        interfaceUsuario.fecharScanner();
        scanner.close();
    }
}
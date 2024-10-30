package projeto.modelo;

public class Financiamento {
    private double valorImovel;
    private int prazoFinanciamento;
    private double taxaJurosAnual;
    private double pagamentoMensal;
    private double totalDoPagamento;

    public Financiamento(double valorImovel, int prazoFinanciamento, double taxaJurosAnual) {
            this.valorImovel = valorImovel;
            this.prazoFinanciamento = prazoFinanciamento;
            this.taxaJurosAnual = taxaJurosAnual;
    }

    public void calcularPagamentoMensal() {
        this.pagamentoMensal = (valorImovel / (prazoFinanciamento * 12)) * (1 + (taxaJurosAnual / 12));
    }
    public void calcularTotalDoPagamento() {
        this.totalDoPagamento = pagamentoMensal * (prazoFinanciamento * 12);
    }

    public void mostrarResultados() {
        System.out.printf("Valor inicial do imovel: %.2f\n", valorImovel);
        System.out.printf("Taxa de juros anual do financiamento: %.2f\n", taxaJurosAnual);
        System.out.printf("Pagamento Mensal: %.2f\n", pagamentoMensal);
        System.out.printf("Pagamento Anual: %.2f\n", pagamentoMensal*12);
        System.out.print("Prazo em anos: " + prazoFinanciamento);
        System.out.printf("\nTotal do Pagamento: %.2f\n", totalDoPagamento);
    }

    /*
setter
    public double setValorImovel() {
        return valorImovel;
    }

    public int setPrazoFinanciamento() {
        return prazoFinanciamento;
    }

    public double setTaxaJurosAnual() {
        return taxaJurosAnual;
    }

    public double setPagamentoMensal() {
        return pagamentoMensal;
    }

    public double setTotalDoPagamento() {
        return totalDoPagamento;
    }
*/

}
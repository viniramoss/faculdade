module com.example.faculdadeexercicios {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens com.example.faculdadeexercicios to javafx.fxml;
    exports com.example.faculdadeexercicios;
}
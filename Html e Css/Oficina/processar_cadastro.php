<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Receba os dados do formulário
    $modelo = $_POST["modelo"];
    $marca = $_POST["marca"];
    $ano = $_POST["ano"];
    $placa = $_POST["placa"];
    $kilometragem = $_POST["kilometragem"];
    $nomeCliente = $_POST["nome"];
    $enderecoCliente = $_POST["endereco"];
    $telefoneCliente = $_POST["telefone"];
    $emailCliente = $_POST["email"];
    $dataCadastro = $_POST["data"];

    // Formate os dados como uma linha CSV
    $linhaCSV = "$modelo,$marca,$ano,$placa,$kilometragem,$nomeCliente,$enderecoCliente,$telefoneCliente,$emailCliente,$dataCadastro\n";

    // Abra o arquivo para escrita (ou crie se não existir)
    $arquivo = fopen("cadastro_carros.csv", "a");

    // Escreva a linha no arquivo
    if ($arquivo) {
        fwrite($arquivo, $linhaCSV);
        fclose($arquivo);
        
        // Redirecione o usuário de volta para a tela inicial
        header("Location: tela_inicial.html");
        exit;
    } else {
        echo "Erro ao abrir o arquivo.";
    }
} else {
    echo "Método de requisição inválido.";
}
?>

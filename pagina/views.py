from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
 
def index(request):
    return render(request, 'pagina/index.html')
 
def paginaInicial(request):
    return render(request, 'pagina/paginaInicial.html')
 
def dashboard(request):
    return render(request, 'pagina/dashboard.html')
 
 
def cadastro(request):
    return render(request, 'pagina/cadastro.html')

def pag(request):
    return render(request, 'pagina/pg1.html')
def pag2(request):
    return render(request, 'pagina/pg2.html')
def pag3(request):
    return render(request, 'pagina/pg3.html')
 
@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')  
        print(f"Recebido do usuário: {user_input}")
 
        time.sleep(3)  # Atraso de 3 segundos na resposta
 
        # Lógica do chatbot
        if user_input == "1":
            response = "Você escolheu a opção 'Endividamento'. Acesse o site para mais informações: <a href='https://www.spcbrasil.org.br/blog/endividamento' target='_blank' class='pink-link' >Clique aqui para saber mais</a>"
        elif user_input == "2":
            response = """
                Você escolheu o Assistente Financeiro! Aqui estão as opções de dicas:<br>
                <div class="option" onclick="sendMessage('1')">1 - Dicas de Planejamento Financeiro</div>
                <div class="option" onclick="sendMessage('2')">2 - Dicas para Reduzir Dívidas</div>
                <div class="option" onclick="sendMessage('3')">3 - Dicas para Poupar e Investir</div>
                <div class="option" onclick="sendMessage('4')">4 - Dicas de Consumo Consciente</div>
                <div class="option" onclick="sendMessage('5')">5 - Dicas de Crédito</div>
            """
 
        elif user_input == "1-1":
            response = " Faça um orçamento mensal detalhado e siga-o rigorosamente."
        elif user_input == "1-2":
            response = "Pague dívidas de maior juros primeiro e renegocie suas condições."
        elif user_input == "1-3":
            response = " Reserve 10% da sua renda mensal para uma poupança ou investimentos."
        elif user_input == "1-4":
            response = " Evite compras impulsivas, avalie a necessidade antes de comprar."
        elif user_input == "1-5":
            response = " Use crédito com responsabilidade, sempre priorizando os juros mais baixos."
        else:
            # retorna menu
            response = """
                <div class="message bot">
                    <div class="profile"></div>
                    <div class="msg">
                        <p>Escolha uma das opções abaixo para começar:</p>
                        <div class="options">
                            <div class="option" onclick="sendMessage('1')">1 - Direcionamento sobre Endividamento</div>
                            <div class="option" onclick="sendMessage('2')">2 - Assistente Financeiro</div>
                        </div>
                    </div>
                </div>
            """
       
       
        # Retorna a resposta como JSON
        return JsonResponse({"response": response})
 
    return JsonResponse({"error": "Método não permitido."}, status=405)
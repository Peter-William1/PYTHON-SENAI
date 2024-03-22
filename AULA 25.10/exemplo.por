
programa {
  inclua biblioteca Util --> u
  funcao inicio() {
    cadeia a, ponto=".", nome,inimigoname,mapa[5][5]
    inteiro op, cde=0, vida=120, dano, critico, cf, experiencia, vidap=100, ataque=0, danoi, inimigo,vidaf
    inteiro sort
    inteiro linha=0, coluna=0
    inteiro ultimaLinha=0, ultimaColuna=0,loop=0
    caracter direcao

    logico luta=falso

    enquanto op!=1
    { 
      escreva("Digite seu nome\n")
      leia(nome)
      u.aguarde(400)
      limpa()
      se (nome=="28064212")
      {
        escreva("28:06:42:06", "\nDo you belive in time travel??\n1.Yes       2.No\n")
        leia(op)
      }
      senao
      {
        escreva("seu nome é: ", nome, "?\nTem certeza?\n1.Sim       2.Não\n")
        leia(op)
      }
      se(op==2)
      {
        limpa()
      }
    }
    u.aguarde(700)
    limpa()
    op=-1
    enquanto (op<0 ou op>4)
    {
      escreva("Bem vindo aventureiro ", nome, "! Primeiramente escolha sua arma!\n1.Arco        2.Espada\n3.Machado     4.Cajado\n")
      leia(op)
  
      
      escolha op 
      {
        caso 1
        a="Arco"
        pare
        caso 2 
        a="Espada"
        pare
        caso 3 
        a="Machado"
        pare
        caso 4 
        a="Cajado"
        caso contrario
        limpa()
        escreva("arma invalida!")
        u.aguarde(700)
        limpa()
        

        
        
      }
    }
    limpa()
    escreva("A arma que voce escolheu foi :", a)
    u.aguarde(500)
    limpa()

    escreva ("Para onde quer ir?\n")

    
    enquanto (cde<=60)
    { 
      
  //Preenchendo a mapa de jogo com zeros
    para (inteiro i=0;i<5;i++){
      para (inteiro j=0;j<5;j++){
        mapa[i][j] = " ▇"
      }
    }
    



    //Lendo um comando para movimentar a personagem
    loop=0
    enquanto(loop==0){

      escreva ("   ⋯ ⋯ ⋯ ⋯ ⋯\n")

      para (inteiro i=0;i<5;i++)
      {
        escreva ("⋮ ")

         para (inteiro j=0;j<5;j++)
         {
           escreva(mapa[i][j])
         }
       escreva("\n")
      }    
      escreva("Digite o comando: ")
      leia(direcao)
      limpa()
      //Verificando qual tecla foi pressionada
      escolha(direcao){
        caso "s": 
          linha++
          pare
        caso "a": 
          coluna--
          pare
        caso "w": 
          linha--
          pare
        caso "d": 
          coluna++
          pare
        caso contrario: 
          pare
      }

      mapa[ultimaLinha][ultimaColuna]=" ▇"
      
      mapa[linha][coluna]="👣"

      limpa()

      escreva ("   ⋯ ⋯ ⋯ ⋯ ⋯\n")
      
      para (inteiro i=0;i<5;i++){
        escreva ("⋮ ")
       para (inteiro j=0;j<5;j++){
          escreva(mapa[i][j])
       }
       escreva("\n")
      }
      ultimaLinha=linha
      ultimaColuna=coluna
      loop++
    }


      vida=120
      escreva("Andando pela floresta.")
      u.aguarde(300)
      escreva(ponto)
      cde= u.sorteia(1, 100)

      u.aguarde(300)
      escreva(ponto)
      u.aguarde(800)
      limpa()
     

      se cde>=70
      {
        escreva("Voce encontrou um inimigo!")

        inimigo=u.sorteia(1,6)
        escolha (inimigo)
        {
          caso 1
          vida=150
          vidaf=150
          inimigoname="Goblin Verde"
          pare

          caso 2
          vida=100
          vidaf=100
          inimigoname="Mago:'Atlantes'"
          pare

          caso 3
          vida=100
          vidaf=100
          inimigoname="Ladrão:'Kuchiki'"
          pare

          caso 4
          vida=120
          vidaf=120
          inimigoname="Caçador"
          pare

          caso 5
          vida=180
          vidaf=180
          inimigoname="Dragão"
          pare
          
          caso 6
          vida=120
          vidaf=120
          inimigoname="Guerreiro:'Damian'"
          pare
        }

        luta=verdadeiro
      }
        se (luta==verdadeiro)
        {
        
          enquanto (vida>=0)
          {
            u.aguarde(700)
            limpa()
            escreva(nome, " ", vidap, "/100","\n", inimigoname,"=", vida, "/", vidaf,"\nOque deseja fazer?\n1.Lutar!     2.Fugir!\n")
            leia(op)
            ataque=u.sorteia(1,100)
           se (ataque<16)
           {
            vidap - u.sorteia(10,20)
           }
            escolha (op)
            {
              caso 1
              se (a=="Arco")
              {
                dano = u.sorteia(1,15)
                critico = u.sorteia(1, 100)
                se (critico<45)
                {
                  escreva("Dano critico !")
                  dano = dano * 2
                }
              }
              se (a=="Espada")
              {
                dano = u.sorteia(1,18)
                critico = u.sorteia(1, 100)
                se (critico<20)
                {
                  escreva("Dano critico !")
                  dano = dano * 2
                }
              }

              se (a=="Cajado")
              {
                dano = u.sorteia(1,11)
                critico = u.sorteia(1, 100)
                se (critico<33)
                {
                  escreva("Dano critico !")
                  dano = dano * 3
                } 
              }
              se (a=="Machado")
              {
                dano = u.sorteia(1,20)
                critico = u.sorteia(1, 100)
                se (critico>60)
                {
                  escreva("Dano critico !")
                  dano = dano * 4
                }
              }
              danoi = u.sorteia(1, 20)
              
              vidap= vidap - danoi
              vida = vida - dano
              
              pare
              caso 2 
              cf = u.sorteia(1, 100)
              se (cf<=26)
              {
                vida=-1
                luta=falso
                limpa()
                escreva("Voce fugiu!")
                cde=0
                u.aguarde(700)
                limpa()
              }
              se vida<=0
              {
                cde=0
                limpa()
                u.aguarde(1000)
              }
            
          
            }
          
          se(vida<=0)
          { 
            se(cf>26)
            {
              u.aguarde(500)
              limpa()
              escreva(nome, "matou um inimigo !")
            }
            u.aguarde(700)
            limpa()
            cde=0
            
          
           }  
           se (vidap<=0)
           {
      
            u.aguarde(700)
            limpa()
            escreva("Voce morreu!")
            u.aguarde(500)
            luta=falso
            
            vida= -1
            limpa()
            escreva("voce deseja continuar?\n1.Sim      2.Não\n")
            leia (op)
            escolha op
            {
             caso 1
              u.aguarde(500)
              limpa()
              escreva("NUNCA DESISTA!")
              luta==verdadeiro
              cde=0
              vida=100
              limpa()
             pare
             caso 2 
              cde=100
              pare 
            }          
          }
    }
  }
}
apps-fileview.texmex_20231012.01_p0
jogorpg.txt
Exibindo jogorpg.txt…
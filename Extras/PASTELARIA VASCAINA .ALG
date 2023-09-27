Algoritmo "Pastelaria Vascaina "

Var
   opm, oplan, qt: inteiro
   pc, p3q, pf, vpc, vp3q, vpf, vtped: real

Inicio

   vpc <- 0
   vp3q <- 0
   vpf <- 0
   vtped <- 0
   
   repita
      escreval("MENU-PRINCIPAL")
      escreval("1-PASTEIS")
      escreval("2-BEBIDAS")
      escreval("3-SOBREMESAS")
      escreval("0-para finalizar")
      leia(opm)
      
      escolha(opm)
         caso 1
            repita
               escreval("PASTEIS")
               escreval("1-Pastel de Carne R$ 17,50")
               escreval("2-Pastel tres queijos R$ 22,50")
               escreval("3-Pastel de Frango R$ 25,00")
               escreval("0-para retornar")
               escreval("digite a opção")
               leia(oplan)

               escolha(oplan)
                  caso 1
                     escreval("digite a quantidade:")
                     leia(qt)
                     pc <- qt * 17.50
                     vpc <- vpc + pc
                  caso 2
                     escreval("digite a quantidade:")
                     leia(qt)
                     p3q <- qt * 22.50
                     vp3q <- vp3q + p3q
                  caso 3
                     escreval("digite a quantidade:" )
                     leia(qt)
                     pf <- qt * 25.00
                     vpf <- vpf + pf
               fimescolha
            ate oplan = 0
         caso 2
         repita
               escreval("BEBIDAS")
               escreval("1-coca cola 2 litros R$ 12.00")
               escreval("2-agua mineral R$ 3.00")
               escreval("3-suco natural diversos R$ 9.00")
               escreval("0-para retornar")
               escreval("digite a opção")
               leia(oplan)

               escolha(oplan)

         caso 3

      fimescolha
   ate opm = 0
   
   vtped <- vpc + vp3q + vpf
   escreval("Total do pedido: R$", vtped)
   
fimalgoritmo
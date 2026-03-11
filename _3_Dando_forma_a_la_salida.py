#El conjuto de estos 8 prints, imprimen una flecha hecha con los asteristcos
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#Si queremos reducir la cantidad de prints podemos usar la variable \n la cual genera 
#un salto de linea despues segun donde se hubiera puesto como el siguiente ejemplo
print("\n",end="----------menor catidad de print----------\n")
print("\n     *\n", "   * *\n", "  *   *\n", " *     *\n", "***   ***\n", "  *   *",)
print("   *   *\n", "  *****\n")

#En las siguientes lienas lo que imprimira en pantalla sera una flecha pero con el 
#doble de grande que la original

print("\n",end="----------Doble de grande----------\n")
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")

#En las siguientes lienas lo que imprimira en pantalla seran dos flechas esto se logra con 
#la varible "string" *n (donde n son las veces que que queremos que se multiplique), la cual 
#en este caso usaremos 3l valor de 2 para duplicar la cadena.
print("\n",end="----------String(Doble)Grande----------\n")
n=2
print("        *        "*n)
print("       * *       "*n)
print("      *   *      "*n)
print("     *     *     "*n)
print("    *       *    "*n)
print("   *         *   "*n)
print("  *           *  "*n)
print(" *             * "*n)
print("******     ******"*n)
print("     *     *     "*n)
print("     *     *     "*n)
print("     *     *     "*n)
print("     *     *     "*n)
print("     *     *     "*n)
print("     *     *     "*n)
print("     *******     "*n)

#Como ejemplo extra haremos lo mismo para la flecha pequeña pero de mas multiplicaciones
#podemos usar diferentes variables para declara las veces que queremos multiplicar no solo 
#se limita con n
print("\n",end="----------String *m pequeño----------\n")
m=3
print("    *    "*m)
print("   * *   "*m)
print("  *   *  "*m)
print(" *     * "*m)
print("***   ***"*m)
print("  *   *  "*m)
print("  *   *  "*m)
print("  *****  "*m)
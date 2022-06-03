import java.math.RoundingMode

fun main() {
    val antCaser = readLine()!!.toInt()

    for (i in 0 until antCaser) {
        val info = readLine()!!.split(" ").map { it.toInt() }
        val hashMap = LinkedHashMap<String, Ingredient>()
        var mainIngredient = ""
        val scalingFactor = info[2].toDouble() / info[1].toDouble()

        for (j in 0 until info[0]) {
            val ingredientInfo = readLine()!!.split(" ")
            val ingredient = Ingredient(ingredientInfo[0], ingredientInfo[1].toDouble(), ingredientInfo[2].toDouble())
            hashMap[ingredientInfo[0]] = ingredient

            with (ingredient) {
                if (percentage == 100.0)
                    mainIngredient = name
            }
        }

        var scalingWeight: Double
        with (hashMap[mainIngredient]!!) {
            weight *= scalingFactor
            scalingWeight = weight
        }

        println("Recipe # ${i + 1}")
        for ((_, ingredient) in hashMap.entries) {
            with (ingredient) {
                weight = (percentage / 100) * scalingWeight
                println("$name ${weight.toBigDecimal().setScale(1, RoundingMode.UP).toDouble()}")
            }
        }
        repeat(40) {
            print("-")
        }
        println()
    }
}

fun repeat(times: Int, action: (Int) -> Unit) {
    for (i in 0 until times) action(times)
}

data class Ingredient(val name: String, var weight: Double, val percentage: Double)
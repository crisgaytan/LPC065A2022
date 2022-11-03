function MyFunction {
    param($veces = 0)
    while ($veces -lt 1) {
	  Write-Host "Hola"
	  $veces++
    }
}
MyFunction

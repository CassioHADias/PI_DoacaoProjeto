document.addEventListener( "DOMContentLoaded", function() {
    const cep = document.getElementById( "cep" );
    if ( cep ) {
        cep.addEventListener( 'change', async ( event ) => {
            let numbers = event.target.value
            if ( numbers ) numbers = numbers.match( /\d+/g )
            if ( numbers ) numbers = numbers.join( '' )
            if ( numbers ) {
                const url = `https://viacep.com.br/ws/${numbers}/json/`
                const response = await fetch( url )
                const data = await response.json()
                if ( data.cep ) {
                    const { logradouro, localidade, uf } = data
                    document.querySelector( '[name="estado"]' ).value = uf
                    document.querySelector( '[name="cidade"]' ).value = localidade
                    document.querySelector( '[name="rua"]' ).value = logradouro
                }
            }
        } )
    }
} )
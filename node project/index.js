const button =document.querySelector('button');
button.addEventListener('click',displaystats);
 function displaystats()
{
    let output='';
    const input = document.getElementById("citys").value
    switch(input){

        case 'delhi':
            pop:123,
            lang:'english and hindi'
            break
        case'pondy':
        output="pop:5520<br>lang:tamil and french";
        break
        case'nagai':
        output="pop:5566<br>lang:tamil"; 
        break  
        default:
            output = "select a city";


    }
        document.querySelector('.result').innerHTML = output;



}
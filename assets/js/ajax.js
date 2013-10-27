// When page has loaded do the following code
$(function(){
	// look for the search box in the base.html file and if you get the  keyup event do the following
    $('#search').keyup(function() {
    	// this is just an AJAX call
        $.ajax({
            type: "POST",
            url: "/articles/search/",// we have already setted it up in urls.py section
            data: { 
                'search_text' : $('#search').val(),//getting value of the search box
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() 						
            },
            success: searchSuccess,// if the it is sucessfull run searchSuccess function
            dataType: 'html'
        });
        
    });

});
// here the code ends
function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}

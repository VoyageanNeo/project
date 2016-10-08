(function($) {                                                                                                                                      
    $.fn.initDateRangePicker = function(start_date_el, end_date_el, future) {                                                                       
        return this.each(function() {                                                                                                               
            var start = moment($(start_date_el).val());                                                                                             
            var end = moment($(end_date_el).val());                                                                                                 

            var display_date = function(start, end) {                                                                                               
                var str = ""                                                                                                                        
                str += start.format('MMMM Do, YYYY');                                                                                               
                str += " - ";                                                                                                                       
                str += end.format('MMMM Do, YYYY');                                                                                                 

                return str;                                                                                                                         
            };                                                                                                                                      

            $(this).find("span").html(display_date(start, end));                                                                                    
            var self = this;                                                                                                                        

            if(!future) {                                                                                                                           
                $(this).daterangepicker({                                                                                                           
                    format: 'YYYY-MM-DD',                                                                                                           
                    timePicker: false,                                                                                                              
                    ranges: {                                                                                                                       
                        'Last 7 days': [moment().subtract('days', 6), moment()],                                                                    
                        'Month to date': [                                                                                                          
                            moment().startOf('month'),                                                                                              
                            moment(),                                                                                                               
                        ],                                                                                                                          
                        'Last Month': [                                                                                                             
                            moment().subtract('month', 1).startOf('month'),                                                                         
                            moment().subtract('month', 1).endOf('month'),                                                                           
                        ]                                                                                                                           
                    },                                                                                                                              
                }, function(start, end) {                                                                                                           
                    $(start_date_el).val(start.format('YYYY-MM-DD'));                                                                               
                    $(end_date_el).val(end.format('YYYY-MM-DD'));                                                                                   

                    $(self).find("span").html(display_date(start, end));                                                                            
                });                                                                                                                                 
            }                                                                                                                                       
            else {                                                                                                                                  
                 $(this).daterangepicker({                                                                                                          
                    format: 'YYYY-MM-DD',                                                                                                           
                    timePicker: false,                                                                                                              
                    ranges: {                                                                                                                       
                        'Next 7 days': [moment().add('days', 1), moment().add('days', 7)],                                                          
                        'Next month': [                                                                                                             
                            moment().add('month', 1).startOf('month'),                                                                              
                            moment().add('month', 1).endOf('month'),                                                                                
                        ],                                                                                                                          
                    },                                                                                                                              
                }, function(start, end) {                                                                                                           
                    $(start_date_el).val(start.format('YYYY-MM-DD'));                                                                               
                    $(end_date_el).val(end.format('YYYY-MM-DD'));                                                                                   

                    $(self).find("span").html(display_date(start, end));                                                                            
                });                                                                                                                                 

            }                                                                                                                                       
        });                                                                                                                                         
    };                                                                                                                                              
}).call(this, jQuery);
$(document).ready(function () {
      $('#sidebarCollapse').on('click', function () {
            $('#sidebar').toggleClass('active');
                });
});

function deleteForm(prefix, btn) {
                var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
                 console.log("total",total)

                if (total > 1) {
                    btn.closest('.form-row').remove();
                    var forms = $('.form-row');
                    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
                    for (var i = 0, formCount = forms.length; i < formCount; i++) {
                        $(forms.get(i)).find(':input').each(function () {
                            updateElementIndex(this, prefix, i);
                        });target
                    }
                }
                return false;
            }

function cloneMore(selector, prefix) {
              var newElement = $(selector).clone(true);
              var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
              console.log("total",total)
              newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function () {
                  var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
                  var id = 'id_' + name;
                  console.log("hmmmmmmmmm",name,id)

                  $(this).attr({
                      'name': name,
                      'id': id
                  }).val('').removeAttr('checked');
              });
              newElement.find('label').each(function () {
                  var forValue = $(this).attr('for');
                  if (forValue) {
                      forValue = forValue.replace('-' + (total - 1) + '-', '-' + total + '-');
                      $(this).attr({
                          'for': forValue
                      });
                  }
              });
              total++;
              $('#id_' + prefix + '-TOTAL_FORMS').val(total);
              $(selector).after(newElement);
              var conditionRow = $('.form-row:not(:last)');
              conditionRow.find('.btn.add-form-row')
                  .removeClass('btn-success').addClass('btn-danger')
                  .removeClass('add-form-row').addClass('remove-form-row')
                  .html('<span class="glyphicon glyphicon-minus" aria-hidden="true" >-</span>');
              return false;
          }

          $(document).on('click', '.add-form-row', function (e) {
          e.preventDefault();
          cloneMore('.form-row:last', 'form');
          return false;
});


function cloneMoreTxt(selector, prefix) {
              var newElement_txt = $(selector).clone(true);

              var total_txt = $('#id_' + prefix + '-TOTAL_FORMS').val();
              console.log("total_txt",total_txt)

              newElement_txt.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function () {
                  var name = $(this).attr('name').replace('-' + (total_txt - 1) + '-', '-' + total_txt + '-');
                  var id = 'id_' + name;
                   console.log("hmmmmmmmmm",name,id)

                  $(this).attr({
                      'name': name,
                      'id': id
                  }).val('').removeAttr('checked');
              });
              newElement_txt.find('label').each(function () {
                  var forValue = $(this).attr('for');
                  if (forValue) {
                      forValue = forValue.replace('-' + (total_txt - 1) + '-', '-' + total_txt + '-');
                      $(this).attr({
                          'for': forValue
                      });
                  }
              });
              total_txt++;
              $('#id_' + prefix + '-TOTAL_FORMS').val(total_txt);
              $(selector).after(newElement_txt);
              var conditionRow = $('.form-row-txt:not(:last)');
              conditionRow.find('.btn.add-txt-row')
                  .removeClass('btn-success').addClass('btn-danger')
                  .removeClass('add-txt-row').addClass('remove-form-row')
                  .html('<span class="glyphicon glyphicon-minus" aria-hidden="true" >-</span>');
              return false;
          }

$(document).on('click', '.add-txt-row', function (e) {
          e.preventDefault();
          cloneMoreTxt('.form-row-txt:last', 'form1');
          return false;
});

function deleteFormTxt(prefix, btn) {
                var total_txt = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
                console.log("dsdsd",total_txt)

                if (total_txt > 1) {

                    btn.closest('.form-row-txt').remove();
                    var forms_txt = $('.form-row-txt');
                    $('#id_' + prefix + '-TOTAL_FORMS').val(forms_txt.length);
                    for (var i = 0, formCount = forms_txt.length; i < formCount; i++) {
                        $(forms_txt.get(i)).find(':input').each(function () {
                            updateElementIndex(this, prefix, i);
                        });target
                    }
                }
                return false;
            }



$(document).on('click', '.remove-form-row', function (e) {
              e.preventDefault();
              deleteForm('form', $(this));
              return false;
});
$(document).on('click', '.remove-form-text', function (e) {
              e.preventDefault();
              deleteFormTxt('form', $(this));
              return false;
});

$(document).ready(function(){
    
})

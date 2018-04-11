$(function () {
    function onFileSelect(e) {
        var
            f = e.target.files[0], // Первый выбранный файл
            reader = new FileReader,
            place = e.path[1]; // Сюда покажем картинку (wrapper)
        ;
        reader.readAsDataURL(f);
        reader.onload = function (e) { // Как только картинка загрузится
            place.style.background = "url('" + e.target.result + "') no-repeat";
            place.style.backgroundSize = "contain";
        }
    }

// проверка поддержки браузером HTML5 Api
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        document.querySelector(".group__file input[type=file]").addEventListener("change", onFileSelect, false);
    } else {
        console.warn("Ваш браузер не поддерживает FileAPI")
    }



    $('.toggle__title').on('click', function () {
       $(this).siblings('.toggle__list').toggleClass('active');
       $(this).toggleClass('active');
    });



    function unique(arr) {
        var result = [];

        nextInput:
            for (var i = 0; i < arr.length; i++) {
                var str = arr[i]; // для каждого элемента
                for (var j = 0; j < result.length; j++) { // ищем, был ли он уже?
                    if (result[j] == str) {
                        continue nextInput; // если да, то следующий
                    }
                }
                result.push(str);
            }

        return result;
    }

    // unique arr for inputs multi

    var listArr = [];

    $('.group__list__item-select').on('click', function () {

        if ($(this).closest('li').hasClass('active') !== true){
            $(this).closest('li').addClass('active');
            listArr.push($(this).data('value'));
        }
        else{
            $(this).closest('li').removeClass('active');
            for (var i = 0; i < listArr.length; i++) {
                if (listArr[i] === $(this).data('value')) {
                    listArr.splice(i, 1);
                }
            }
        }
        listArr = unique(listArr);
        $(this).closest('.toggle__list').find('input[type="hidden"]').val(listArr);
    });


    // unique arr for inputs multi

    var listFriendArr = [];
    var listAdminArr = [];
    $('.group__status').on('click', function () {




        if ($(this).hasClass('success-icon') !== true){

            $(this).addClass('success-icon');

            if($(this).closest('.toggle__list').hasClass('group__addfriends')){
                listFriendArr.push($(this).closest('li').data('value'));
            }

            if($(this).closest('.toggle__list').hasClass('group__addadmin')){
                listAdminArr.push($(this).closest('li').data('value'));
            }
        }
        else{
            $(this).removeClass('success-icon');

            if($(this).closest('.toggle__list').hasClass('group__addfriends')){
                for (var i = 0; i < listFriendArr.length; i++) {
                    if (listFriendArr[i] === $(this).closest('li').data('value')) {
                        listFriendArr.splice(i, 1);
                    }
                }
            }
            if($(this).closest('.toggle__list').hasClass('group__addadmin')){
                for (var i = 0; i < listAdminArr.length; i++) {
                    if (listAdminArr[i] === $(this).closest('li').data('value')) {
                        listAdminArr.splice(i, 1);
                    }
                }
            }

        }
        listFriendArr = unique(listFriendArr);
        listAdminArr = unique(listAdminArr);

        if($(this).closest('.toggle__list').hasClass('group__addfriends')){
            $(this).closest('.toggle__list').find('input[type="hidden"]').val(listFriendArr);
        }

        if($(this).closest('.toggle__list').hasClass('group__addadmin')){
            $(this).closest('.toggle__list').find('input[type="hidden"]').val(listAdminArr);
        }

    });



});
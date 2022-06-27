<?php

/**
 * Контроллер администраторов
 *
 */

// Подключаем модели
include_once 'models/ModersModel.php';
include_once 'models/CompaniesModel.php';
include_once 'models/EmployersModel.php';
include_once 'models/ApplicantsModel.php';
include_once 'models/UsersModel.php';

/**
 * Формирование главной страницы сайта
 *
 * @param object $smarty шаблонизатор
 */

 function indexAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }
        $pageTitle = "Главная страница админ-панели";

        $companies = getAllCompsForAdmin();

		include_once 'views/admin/index.tpl';
	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function viewonecompAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }

        if (isset($_GET['id'])) {
            $compInfo = getOneCompInfoById($_GET['id']);
            $pageTitle = "Страница работы с компанией ".$compInfo["company-name"];

            $compEmpls = getEmplsByCompId($_GET['id']);

            include_once 'views/admin/viewonecomp.tpl';
        } else {
            $companies = getAllCompsForAdmin();
            $pageTitle = "Страница работы с компаниями";

            include_once 'views/admin/viewallcomp.tpl';
        }
	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function viewoneemplAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }

        if (isset($_GET['id'])) {
            $emplInfo = getOneEmplInfoById($_GET['id']);
            $pageTitle = "Страница работы с вакансией ".$emplInfo["career-objective"];

            $compInfo = getOneCompInfoById($emplInfo['company-id']);

            include_once 'views/admin/viewoneempl.tpl';
        } else {
            $empls = getAllEmplsForAdmin();
            $pageTitle = "Страница работы с вакансиями";

            include_once 'views/admin/viewallempl.tpl';
        }


	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function applicantsAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }

        if (isset($_GET['id'])) {
            $applInfo = getOneApplInfoById($_GET['id']);
            $pageTitle = "Страница работы с резюме ".$applInfo["career-objective"];

            // вытаскиваю другие резюме пользователя
            $otherAppls = getOtherApplsOfUser($applInfo['tg-id'], $_GET['id']);

            include_once 'views/admin/applicants.tpl';
        } else {
            $applicants = getAllApplsForAdmin();
            $pageTitle = "Страница работы с резюме";

            include_once 'views/admin/applicants.tpl';
        }


	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function modersAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }

        $moders = getAllModersForAdmin();
        $pageTitle = "Страница управление ролями пользователей";

        $allUsers = getAllUsers();

        include_once 'views/admin/moders.tpl';
	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function endmoderAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }

        $moders = deleteModerById($_GET['id']);

        JSRedirect('/admin/moders/');
	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function addmoderAction () {
	if (isset($_SESSION['auth']) AND $_SESSION['auth'] == 1) {
		if ($_SESSION['status'] == 'admin') {
          $status = 'администратор';
        } else {
          $status = 'модератор';
        }

        if (isset($_POST['login'])) {
            if (!empty($_POST['login']) AND !empty($_POST['password'])) {
                $checkLoginSymb = checkLoginSymb($_POST['login']);
        		if ($checkLoginSymb == 1) {
        			$checkPass = checkPassSymb($_POST['password']);
        			if ($checkPass == 1) {
                        // если нет претензий к введенным логину и паролю
                        $cryptPass = crypt($_POST['password'], "hg56ij89erf45dh");
                        $userInfo = getUserInfoByTGID($_GET['id']);
                        addNewModer($_GET['id'], $userInfo['tg-login'], $_POST['login'], $cryptPass);
                        updtUserStatusToModer($_GET['id']);
                        JSRedirect('/admin/addmoder/'.$_GET['id'].'/');
                    } else {
        				$_SESSION['checkUsrWrong'] = "Вы использовали в пароле недопустимые символы";
        				JSRedirect('/admin/addmoder/'.$_GET['id'].'/');
                    }
                } else {
        			$_SESSION['checkUsrWrong'] = "Вы использовали в логине недопустимые символы. Допустимы только буквы, цифры и символы - и _";
        			JSRedirect('/admin/addmoder/'.$_GET['id'].'/');
        		}
            } else {
                // если поле с именем пользователя или пароля пустое, выдаем ошибку
        		$_SESSION['checkUsrWrong'] = "Вы не ввели имя пользователя или пароль!";
        		JSRedirect('/admin/addmoder/'.$_GET['id'].'/');
            }
        } else {
            $userInfo = getUserInfoByTGID($_GET['id']);
            $pageTitle = "Страница назначения модератором ".$userInfo['firstname'];
        }


        include_once 'views/admin/addmoder.tpl';
	} else {
		include_once 'views/admin/login.tpl';
		unset($_SESSION['checkUsrWrong']);
	}

 }

 function checkLoginSymb ($login) {
	 if (preg_match('/^[a-zA-Z][a-zA-Z0-9-_]{1,20}$/', $login)) {
		return 1;
	} else {
		return 2;
	}
 }

 function checkPassSymb ($password) {
	/*if (preg_match('/(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/', $password)) {
		return 1;
	} else {
		return 2;
	}*/
	if (preg_match('/[0-9A-Za-z_!@#=%-]{6,14}$/', $password)) {
		return 1;
	} else {
		return 2;
	}
 }


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $pageTitle; ?> | Nifty - Admin Template</title>


    <!--STYLESHEET-->
    <!--=================================================-->

    <!--Open Sans Font [ OPTIONAL ] -->
     <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700&amp;subset=latin" rel="stylesheet">


    <!--Bootstrap Stylesheet [ REQUIRED ]-->
    <link href="/templates/admin/css/bootstrap.min.css" rel="stylesheet">


    <!--Nifty Stylesheet [ REQUIRED ]-->
    <link href="/templates/admin/css/nifty.min.css" rel="stylesheet">


    <!--Premium Icons [ OPTIONAL ]-->
    <link href="/templates/files/premium/icon-sets/icons/line-icons/premium-line-icons.min.css" rel="stylesheet">
    <link href="/templates/files/premium/icon-sets/icons/solid-icons/premium-solid-icons.min.css" rel="stylesheet">


    <!--JAVASCRIPT-->
    <!--=================================================-->

    <!--Page Load Progress Bar [ OPTIONAL ]-->
    <link href="/templates/admin/css/pace.min.css" rel="stylesheet">
    <script src="/templates/admin/js/pace.min.js"></script>


    <!--jQuery [ REQUIRED ]-->
    <script src="/templates/admin/js/jquery.min.js"></script>


    <!--BootstrapJS [ RECOMMENDED ]-->
    <script src="/templates/admin/js/bootstrap.min.js"></script>


    <!--Nifty Admin [ RECOMMENDED ]-->
    <script src="/templates/admin/js/nifty.min.js"></script>


    <!--=================================================

    REQUIRED
    You must include this in your project.


    RECOMMENDED
    This category must be included but you may modify which plugins or components which should be included in your project.


    OPTIONAL
    Optional plugins. You may choose whether to include it in your project or not.


    Detailed information and more samples can be found in the document.

    =================================================-->





</head>

<!--TIPS-->
<!--You may remove all ID or Class names which contain "demo-", they are only used for demonstration. -->

<body>
    <div id="container" class="effect mainnav-lg">

        <?php include_once('navbar.tpl'); ?>

        <div class="boxed">

            <!--CONTENT CONTAINER-->
            <!--===================================================-->
            <div id="content-container">

                <!--Page Title-->
                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                <div id="page-title">
                    <h1 class="page-header text-overflow">Вы вошли как <?php echo $status; ?></h1>

                    <!--Searchbox-->
                    <div class="searchbox">
                        <div class="input-group custom-search-form">
                            <input type="text" class="form-control" placeholder="Search..">
                            <span class="input-group-btn">
                                <button class="text-muted" type="button"><i class="pli-magnifi-glass"></i></button>
                            </span>
                        </div>
                    </div>
                </div>
                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                <!--End page title-->


                <!--Breadcrumb-->
                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                <ol class="breadcrumb">
                    <li><a href="/admin/">Главная</a></li>
                    <?php
                    if (isset($_GET['id'])) {
                        ?>
                        <li><a href="/admin/applicants/">Работа с резюме</a></li>
                        <li class="active">Резюме <?php echo  $applInfo["firstname"]." ".$applInfo["lastname"]; ?></li>
                        <?php
                    } else {
                        ?>
                        <li class="active">Работа с резюме</li>
                        <?php
                    }
                    ?>
                </ol>
                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                <!--End breadcrumb-->




                <!--Page content-->
                <!--===================================================-->
                <div id="page-content">


					<!-- QUICK TIPS -->
					<!-- ==================================================================== -->
					<h2>Вы на странице работы с резюме</h2>
                    <br>
                    <h3>Резюме пользователя <?php echo  $applInfo["firstname"]." ".$applInfo["lastname"]." ".$applInfo["patronymic"]; ?></h3>
                    <?php
                    if (isset($_GET['id'])) {
                        if ($applInfo == Null) {
                            ?>
                            <p>Такое резюме не найдено.</p>
                            <?php
                        } else {
                            ?>
                            <div class="table-responsive">
        					    <table class="table">
        					        <tbody>
                                        <tr>
        					                <th>Логин телеграм</th>
        					                <th>Имя</th>
        					                <th>Направление деятельности</th>
        					                <th>Форма обучения</th>
        					                <th>Желаемая должность</th>
        					                <th>Желаемая зарплата</th>
        					                <th>Город</th>
        					                <th>Возможность работать удаленно</th>
        					                <th>Готовность к переезду</th>
        					                <th>Опыт работы</th>
        					                <th>Предпочтительный график работы</th>
        					                <th>Телефон</th>
        					            </tr>
                                        <tr>
            					            <td><?php echo  $applInfo["tg-login"]; ?></td>
            					            <td><?php echo  $applInfo["firstname"]." ".$applInfo["lastname"]." ".$applInfo["patronymic"]; ?></td>
            					            <td><?php echo  $applInfo["line-business"]; ?></td>
            					            <td><?php echo  $applInfo["education-form"]; ?></td>
            					            <td><?php echo  $applInfo["career-objective"]; ?></td>
            					            <td><?php echo  $applInfo["desired-salary"]; ?></td>
            					            <td><?php echo  $applInfo["city-work"]; ?></td>
            					            <td><?php echo  $applInfo["distant-work"]; ?></td>
            					            <td><?php echo  $applInfo["relocate"]; ?></td>
            					            <td><?php echo  $applInfo["work-experience"]; ?></td>
            					            <td><?php echo  $applInfo["desired-work-schedule"]; ?></td>
            					            <td><?php echo  $applInfo["phone"]; ?></td>
            					        </tr>
        					        </tbody>
        					    </table>
        					</div>
                            <br>
        					<a href="#" class="btn btn-dark">Сохранить изменения</a>
        					<br><br><br>
                            <h3>Другие резюме пользователя</h3>
                            <?php
                            if ($otherAppls == Null) {
                                ?>
                                <p>Других резюме пользователя не найдено.</p>
                                <?php
                            } else {
                                ?>
                                <div class="table-responsive">
            					    <table class="table">
            					        <tbody>
                                            <tr>
            					                <th>Логин телеграм</th>
            					                <th>Имя</th>
            					                <th>Направление деятельности</th>
            					                <th>Форма обучения</th>
            					                <th>Действие</th>
            					            </tr>
                                            <?php
                                            foreach ($otherAppls as $item) {
                                                ?>
                                                <tr>
                					                <td><?php echo  $item["tg-login"]; ?></td>
                					                <td><?php echo  $item["firstname"]." ".$item["lastname"]; ?></td>
                					                <td><?php echo  $item["line-business"]; ?></td>
                					                <td><?php echo  $item["education-form"]; ?></td>
                					                <td><a href="/admin/applicants/<?php echo  $item['id']; ?>/" class="btn btn-info">Смотреть полностью</a></td>
                					            </tr>
                                                <?php
                                            }
                                            ?>
            					        </tbody>
            					    </table>
            					</div>
                                <?php
                            }
                        }
                    } else {
                        if ($applicants == Null) {
                            ?>
                            <p>Резюме в базе не найдены.</p>
                            <?php
                        } else {
                            ?>
                            <div class="table-responsive">
        					    <table class="table">
        					        <tbody>
                                        <tr>
        					                <th>Логин телеграм</th>
        					                <th>Имя</th>
        					                <th>Направление деятельности</th>
        					                <th>Форма обучения</th>
        					                <th>Действие</th>
        					            </tr>
                                        <?php
                                        foreach ($applicants as $item) {
                                            ?>
                                            <tr>
            					                <td><?php echo  $item["tg-login"]; ?></td>
            					                <td><?php echo  $item["firstname"]." ".$item["lastname"]; ?></td>
            					                <td><?php echo  $item["line-business"]; ?></td>
            					                <td><?php echo  $item["education-form"]; ?></td>
            					                <td><a href="/admin/applicants/<?php echo  $item['id']; ?>/" class="btn btn-info">Смотреть полностью</a></td>
            					            </tr>
                                            <?php
                                        }
                                        ?>
        					        </tbody>
        					    </table>
        					</div>
                            <?php
                        }
                    }
                    ?>
					<!-- ==================================================================== -->
					<!-- END QUICK TIPS -->



                </div>
                <!--===================================================-->
                <!--End page content-->


            </div>
            <!--===================================================-->
            <!--END CONTENT CONTAINER-->



            <?php include_once('mainnavigation.tpl'); ?>

            <!--ASIDE-->
            <!--===================================================-->
            <aside id="aside-container">
                <div id="aside">
                    <div class="nano">
                        <div class="nano-content">

                            <!--Nav tabs-->
                            <!--================================-->
                            <ul class="nav nav-tabs nav-justified">
                                <li class="active">
                                    <a href="#demo-asd-tab-1" data-toggle="tab">
                                        <i class="pli-speech-bubble-7"></i>
                                    </a>
                                </li>
                                <li>
                                    <a href="#demo-asd-tab-2" data-toggle="tab">
                                        <i class="pli-information"></i>
                                        Reports
                                    </a>
                                </li>
                                <li>
                                    <a href="#demo-asd-tab-3" data-toggle="tab">
                                        <i class="pli-wrench"></i>
                                        Settings
                                    </a>
                                </li>
                            </ul>
                            <!--================================-->
                            <!--End nav tabs-->



                            <!-- Tabs Content -->
                            <!--================================-->
                            <div class="tab-content">

                                <!--First tab-->
                                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                                <div class="tab-pane fade in active" id="demo-asd-tab-1">
                                    <p class="pad-all text-lg">First tab</p>
                                    <div class="pad-hor">
                                        Lorem ipsum dolor sit amet, consectetuer adipiscing elit,
                                        sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
                                        Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl
                                        ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate
                                        velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan
                                        et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
                                    </div>
                                </div>
                                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                                <!--End first tab-->


                                <!--Second tab-->
                                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                                <div class="tab-pane fade" id="demo-asd-tab-2">
                                    <p class="pad-all text-lg">Second tab</p>
                                    <div class="pad-hor">
                                        Lorem ipsum dolor sit amet, consectetuer adipiscing elit,
                                        sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
                                        Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl
                                        ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate
                                        velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan
                                        et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
                                    </div>
                                </div>
                                <!--End second tab-->
                                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->


                                <!--Third tab-->
                                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                                <div class="tab-pane fade" id="demo-asd-tab-3">
                                    <p class="pad-all text-lg">Third tab</p>
                                    <div class="pad-hor">
                                        Lorem ipsum dolor sit amet, consectetuer adipiscing elit,
                                        sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
                                        Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl
                                        ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate
                                        velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan
                                        et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
                                    </div>
                                </div>
                                <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->

                            </div>
                        </div>
                    </div>
                </div>
            </aside>
            <!--===================================================-->
            <!--END ASIDE-->

        </div>



        <!-- FOOTER -->
        <!--===================================================-->
        <footer id="footer">

            <!-- Visible when footer positions are fixed -->
            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
            <div class="show-fixed pull-right">
                You have <a href="#" class="text-bold text-main"><span class="label label-danger">3</span> pending action.</a>
            </div>



            <!-- Visible when footer positions are static -->
            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
            <div class="hide-fixed pull-right pad-rgt">
                14GB of <strong>512GB</strong> Free.
            </div>



            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
            <!-- Remove the class "show-fixed" and "hide-fixed" to make the content always appears. -->
            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

            <p class="pad-lft">&#0169; 2017 Your Company</p>



        </footer>
        <!--===================================================-->
        <!-- END FOOTER -->


        <!-- SCROLL PAGE BUTTON -->
        <!--===================================================-->
        <button class="scroll-top btn">
            <i class="pci-chevron chevron-up"></i>
        </button>
        <!--===================================================-->



    </div>
    <!--===================================================-->
    <!-- END OF CONTAINER -->



    </body>
</html>

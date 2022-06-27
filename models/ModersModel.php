<?php
function getAllModersForAdmin () {

	$sql = "SELECT * FROM `moders`";


	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	$query0 = mysqli_num_rows($query);
	if ($query0 > 0) {
		while ($row = mysqli_fetch_assoc($query)) {
	    $rsArray[] = $row;
		}
	} else {
		$rsArray = Null;
	}

	return $rsArray;

	mysqli_close($db);
}

function addNewModer ($tgId, $tgLogin, $login, $password) {
	$sql = "INSERT INTO `moders` (`tg-id`, `tg-login`, `login`, `password`) VALUES ('{$tgId}', '{$tgLogin}', '{$login}', '{$password}')";
	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	return $query;

	mysqli_close($db);
}

function deleteModerById ($id) {
	$sql = "DELETE FROM `moders` WHERE `id` = '{$id}'";
	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	return $query;

	mysqli_close($db);
}

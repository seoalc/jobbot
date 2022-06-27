<?php
function getAllUsers () {

	$sql = "SELECT * FROM `users` WHERE `status` = 0";


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

function getUserInfoByTGID ($tgId) {
	$sql = "SELECT * FROM `users` WHERE `tg-id` = '{$tgId}'";
	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	$row = mysqli_fetch_assoc($query);
	return $row;

	mysqli_close($db);
}

function updtUserStatusToModer ($tgId) {
	$sql = "UPDATE `users` SET `status` = 2 WHERE `tg-id` = '{$tgId}'";
	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	return $query;

	mysqli_close($db);
}

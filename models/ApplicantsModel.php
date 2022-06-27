<?php
function getAllApplsForAdmin () {

	$sql = "SELECT * FROM `applicants`";


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

function getOneApplInfoById ($id) {
	$sql = "SELECT * FROM `applicants` WHERE `id` = '{$id}'";
	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	$row = mysqli_fetch_assoc($query);
	return $row;

	mysqli_close($db);
}

function getOtherApplsOfUser ($tgId, $id) {

	$sql = "SELECT * FROM `applicants` WHERE `tg-id` = {$tgId} AND `id` != {$id}";


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

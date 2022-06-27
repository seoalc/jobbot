<?php
function getAllEmplsForAdmin () {

	$sql = "SELECT * FROM `employers`";


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

function getEmplsByCompId ($compId) {

	$sql = "SELECT * FROM `employers` WHERE `company-id` = {$compId}";


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

function getOneEmplInfoById ($id) {
	$sql = "SELECT * FROM `employers` WHERE `id` = '{$id}'";
	$db = mysqli_connect("localhost", "root", "pass", "jobbot");

	$query = mysqli_query($db, $sql);
	$row = mysqli_fetch_assoc($query);
	return $row;

	mysqli_close($db);
}

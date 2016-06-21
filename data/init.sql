CREATE TABLE IF NOT EXISTS tasks( 
	id INTEGER PRIMARY KEY,
	node_id INTERGER NOT NULL default 0,
	name TEXT NOT NULL default 'no name',
	description TEXT default '',
	status INTEGER DEFAULT 0 );

 CREATE TABLE IF NOT EXISTS pomodores( 
	id INTEGER PRIMARY KEY,
	task_id INTERGER NOT NULL,
	date TEXT NOT NULL ); 
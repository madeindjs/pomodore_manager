﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Ajax;

using Reports_Manager.Models;


namespace Reports_Manager.Controllers
{
    public class UsersController : Controller
    {
        private CarrierDataEntities database = new CarrierDataEntities() ;

        // GET: users/index
        public ActionResult Index()
        {
            var users_data = database.Users.ToList();
            return View(users_data);
        }

    }
}

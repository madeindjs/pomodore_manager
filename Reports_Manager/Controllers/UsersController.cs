using System;
using System.Collections.Generic;
using System.Linq;
using System;
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
        private User _user_table = new User();

        // GET: users/index
        public ActionResult Index()
        {
            return View();
        }

    }
}

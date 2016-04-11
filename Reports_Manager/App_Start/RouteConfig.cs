using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace Reports_Manager
{
    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
                name: "signin",
                url: "signin",
                defaults: new { controller = "Sessions", action = "Create" }
            );

            routes.MapRoute(
                name: "signup",
                url: "signup",
                defaults: new { controller = "Users", action = "Create" }
            );

            routes.MapRoute(
                name: "signout",
                url: "signout",
                defaults: new { controller = "Sessions", action = "Delete" }
            );

            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Shops", action = "Index", id = UrlParameter.Optional }
            );
        }
    }
}
